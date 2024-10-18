# -*- coding: utf-8 -*-

{
    'name': "Integer Widget",
    'version': '1.0',
    'installable': True,
    'application': True,
    'depends': ['base'],
    'assets': {
        'web.assets_backend': [
            'integer_widget/static/src/xml/field_template.xml',
            'integer_widget/static/src/js/integer_widget.js'
        ]
    }

}