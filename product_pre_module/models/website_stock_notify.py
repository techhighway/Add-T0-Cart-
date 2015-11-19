from openerp.osv import fields, osv
import time
import datetime
import os
from openerp.tools.translate import _
from openerp import netsvc


class product_product(osv.osv):
    _inherit = "product.product"
    
    
    def check_for_product_attribute(self, cr, uid, ids, field_name, arg, context=None):
        ## TO CHECK IS PRODUCT HAVE VARIANT OR NOT AND HIDE ACTIVE BUTTON
        
        res = {}
        for product_id in self.browse(cr, uid, ids, context=context):
            attribute_value_ids = self.browse(cr, uid, ids, context=context).attribute_value_ids
            if not attribute_value_ids:
                res[product_id.id] = True
            else:
                res[product_id.id] = False
        return res
    
    _columns = {
                'is_having_attribute':fields.function(check_for_product_attribute, method=True, string='Boolean Field', type='boolean'),
                }
product_product()

