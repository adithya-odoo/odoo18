# -*- coding: utf-8 -*-

{
    'name': 'Quality Assurance',
    'version': '18.0.1.0.0',
    'installable': True,
    'application': True,

    'depends': ['base',
                'product',
                'stock',
                'purchase'],
    'data': [
        'security/quality_security.xml',
        'security/ir.model.access.csv',
        'views/quality_measure_view.xml',
        'views/quality_alert_view.xml',
        'views/quality_test_view.xml',
        'views/stock_view.xml',
    ],
    'license': 'LGPL-3',
}
