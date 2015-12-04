{
    'name': 'Disable Product Variant Activation Checkbox',
    'category': 'website',
    'summary': 'This module deactive, active field on product variant form for product which does not have product variant',
    'website': 'https://www.techhighway.co.in',
    'version': '1.0',
    'description': """

        """,
    	'author'	: 'TechHighway Systems Pvt. Ltd.',
        'depends'    : [ 'website', 'sale','website_sale', 'payment'],
    	'data'	    : [
                        'views/product_variant_view.xml',
    		          ],
    	'installable': True,
    	'application': True,
}
