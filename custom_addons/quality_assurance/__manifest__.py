# -*- coding: utf-8 -*-

{
    'name': "Quality Assurance",
    'version': '18.0.1.0.0',
    'application': True,

    'depends': ['base',
                'purchase',
                'stock'],

    'data': [
        'security/ir.model.access.csv',
        'views/quality_assurance.xml',
        'views/quality_alert.xml'
    ],
    'license': 'LGPL-3',
}

