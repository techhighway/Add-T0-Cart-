
# -*- coding: utf-8 -*-
import werkzeug

from openerp import SUPERUSER_ID
from openerp import http
from openerp.http import request
from openerp.tools.translate import _
from openerp.addons.website.models.website import slug
from openerp import http
import json

PPG = 20 # Products Per Page
PPR = 4  # Products Per Row

    
class MyController(http.Controller):
    
    # FOR THE DEFAULT (NON-INHERITED) "ADD TO CART" METHODS
    # ADDING TRY-EXCEPT FOR EMPTY VALUE "ADD TO CART" ACTION BY USER
    @http.route(['/shop/cart/update'], type='http', auth="public", methods=['POST'], website=True)
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        cr, uid, context = request.cr, request.uid, request.context
        try:
            add_qty = float(add_qty)
        except:
            if request.httprequest.headers and request.httprequest.headers.get('Referer'):
                return request.redirect(str(request.httprequest.headers.get('Referer')))
            return request.redirect('/shop')
        request.website.sale_get_order(force_create=1)._cart_update(product_id=int(product_id), add_qty=add_qty, set_qty=float(set_qty))
        return request.redirect("/shop/cart")

    @http.route(['/shop/cart/update_no_redirect'], type='http', auth="public", methods=['GET'], website=True)
    def cart_update_no_redirect(self, product_id, add_qty=1, set_qty=0, **kw):
        # HANDLING INVALID "add_qty" VALUES
        
        try:
            add_qty = float(add_qty)
        except ValueError:
            #this.do_warn(_t("The following fields are invalid:"), warnings.join(''));
            return None
        if add_qty <= 0.0:
            return None
        cr, uid, context = request.cr, request.uid, request.context
        request.website.sale_get_order(force_create=1)._cart_update(product_id=int(product_id), add_qty=add_qty, set_qty=float(set_qty))
        if request.httprequest.headers and request.httprequest.headers.get('Referer'):
            return request.redirect(str(request.httprequest.headers.get('Referer')))
        return request.redirect('/shop')
    
    @http.route(['/shop/cart/update_json_shop_to_qty'], type='json', auth="public", methods=['POST'], website=True)
    def update_shop_to_cart_qty_json(self, product_id, add_qty=None, set_qty=None, display=True):
        if set_qty:
            try:
                set_qty = float(set_qty)
            except ValueError:
                return None
            if set_qty <= 0.0:
                return None
        order = request.website.sale_get_order(force_create=1)
        if order:
            value = {}
            so_line_obj = request.registry['sale.order.line']
            #so_line_obj = request.session.model('sale.order.line')
            cr, uid, context = request.cr, request.uid, request.context
            if 1:#try:
                product_id = int(product_id)
            #except ValueError:
            #    return None
            so_line_ids = so_line_obj.search_read(cr, SUPERUSER_ID, [('order_id', '=', order.id), ('product_id', '=', product_id)], ['id'], context=context)
            if so_line_ids:
                value = order._cart_update(product_id=product_id, line_id=so_line_ids[0]['id'], add_qty=add_qty, set_qty=set_qty)
            if not display:
                return None
            value['cart_quantity'] = order.cart_quantity
            value['quantity'] = set_qty
            value['website_sale.total'] = request.website._render("website_sale.total", {
                    'website_sale_order': request.website.sale_get_order()
                })
            return value
        return None
    
    @http.route(['/shop/get_cart_qty_for_selected_variant'], type='http', auth="public", website=True)
    def get_cart_qty_for_selected_variant(self, product_id=False):
        data ={}
        if product_id.isdigit():
            product_uom_qty = 0.0
            data["selected_product_variant_uom_qty"] = False
            data["product_id"] = int(product_id)
            order = request.website.sale_get_order(force_create=1)
            if order:
                so_line_obj = request.registry['sale.order.line']
                cr, uid, context = request.cr, request.uid, request.context
                so_line_qtys = so_line_obj.search_read(cr, SUPERUSER_ID, [('order_id', '=', order.id), ('product_id', '=', data["product_id"])], ['product_uom_qty'], context=context)
                for so_line_qty in so_line_qtys:
                    product_uom_qty += so_line_qty['product_uom_qty']
                if product_uom_qty:
                    data["selected_product_variant_uom_qty"] = product_uom_qty
        return  json.dumps(data)


    # IF IN CASE, THE QUOTATION REFERRED BY SESSION OBJECT IN BELOW METHOD IS DELETED AND WE REFRESH THE PAGE,
    # NILESH WANT THAT THE ERROR SHOULD NOT SHOWN INSTEAD WE SHOUDL BE REDIRECTED TO THE "/SHOP" PAGE
    @http.route(['/shop/confirmation'], type='http', auth="public", website=True)
    def payment_confirmation(self, **post):
        """ End of checkout process controller. Confirmation is basically seing
        the status of a sale.order. State at this point :

         - should not have any context / session info: clean them
         - take a sale.order id, because we request a sale.order and are not
           session dependant anymore
        """
        cr, uid, context = request.cr, request.uid, request.context
        sale_order_id = request.session.get('sale_last_order_id')
        if sale_order_id:
            order = request.registry['sale.order'].browse(cr, SUPERUSER_ID, sale_order_id, context=context)
        else:
            return request.redirect('/shop')
        try:
            # IF STATE IS CANCELLED, REDIRECT TO "/SHOP" 
            # IF THE QUOTATION IS DELETED, THIS WILL GENERATE AN ERROR AND WILL INTURN REDIRECT TO "/SHOP"
            if order.state == u'cancel':
                return request.redirect('/shop')
            return request.website.render("website_sale.confirmation", {'order': order})
        except:
            # ON EXCEPTION, MEANS SOMETHING IS NOT GOOD, WE REDIRECT TO "/SHOP"
            return request.redirect('/shop')
        
        
