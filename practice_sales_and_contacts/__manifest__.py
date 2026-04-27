{
    'name': 'Sales and Contacts Practice',
    'version': '1.0',
    'description': """
Odoo Sale Order and Contacts Practice.
=====================================
""",
    'depends': ['base','sale_management','account','contacts'],
    'data':[
        "views/res_partner_views.xml",
        "data/contact_sequence.xml",
        "views/product_template_views.xml",
        "views/sale_order_views.xml"
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'sequence': 1,
}