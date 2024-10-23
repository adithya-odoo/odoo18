# -*- coding: utf-8 -*-

{
    'name': "Order Type",
    'version': '1.0',

    'depends': ['base',
                'point_of_sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/settings.xml',
        'views/pos_order.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'order_type/static/src/xml/order_type.xml',
            'order_type/static/src/xml/order_reciept.xml',
            'order_type/static/src/js/order_type.js',
            'order_type/static/src/js/order_reciept.js',
            ],
    },
    'license': 'LGPL-3',
}

