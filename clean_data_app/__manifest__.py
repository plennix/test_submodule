# -*- coding: utf-8 -*-
{
    'name': 'Bulk Clear/Clean Records and Data',
    "author": "Edge Technologies",
    'version': '16.0.1.0',
    'description': """ 
        Mass clean data for wizard
    """,
    "summary" : 'Mass clear data mass delete data mass clean data bulk clear data bulk delete data bulk clean data clean database clean demo data mass clear records mass delete records mass clean records bulk clear records bulk delete records bulk clean records',
    'live_test_url': "https://youtu.be/iJkJ3BnbXbM",
    "images":["static/description/main_screenshot.png"],
    "license" : "OPL-1",
    'depends': ['base','sale_management','stock','purchase'],
    'data': [ 
        'security/ir.model.access.csv',
        'wizard/delete_data.xml',
            ],
    'installable': True,
    'auto_install': False,
    'price': 4,
    'currency': "EUR",
    'category': 'Tools',

}
