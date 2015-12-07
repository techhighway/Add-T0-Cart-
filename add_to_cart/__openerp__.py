{
    'name': 'Add To Cart',
    'category': 'Website',
    'summary': 'Sell Your Products Online with ease.',
    'website': 'https://www.techhighway.co.in',
    'version': '1.0',
    'description': """
OpenERP E-Commerce
==================

        """,
    	'author'	: 'TechHighway Systems Pvt. Ltd.',
        'depends'	: [ 'website', 'sale','website_sale', 'payment' ],
    	'data'	    : [
	                    'views/add_to_cart_template_view.xml',
    		          ],
	'images': ['static/description/add2cart_prod_kanban_view.png'],	 
    	'installable': True,
    	'application': True,
}
