# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'XLSX Import',
    'summary': 'XLSX Import',
    'description': """
    	XLSX Import of customer,supplier and product

	""",
    'version': '14.1.1',
    'depends': ['base','account','contacts','sale_management'],
    'data' : [
        'security/ir.model.access.csv',
        'views/partner_view.xml',  
        'views/product_view.xml',     
        'wizard/update_customer.xml',
        'wizard/update_product.xml',
        
     ],
    'test': [
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,

}
