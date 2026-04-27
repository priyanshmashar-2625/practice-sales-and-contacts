{
    'name': 'Sales and Contacts Practice',
    'version': '1.0',
    'description': """
Odoo Sale Order and Contacts Practice.
=====================================
""",
    'depends': ['base','sale','sale_management','account'],
    'data':[
        "views/res_partner_views.xml"
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'sequence': 1,
}