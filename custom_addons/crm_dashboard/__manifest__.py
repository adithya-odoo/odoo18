# -*- coding: utf-8 -*-

{
    'name': "Crm Dashboard",
    'version': '1.0',
    'installable': True,
    'depends': ['base',
                'crm',
                 'sale'],
    'data':[
        'views/crm_dashboard_menu.xml',
        'views/crm_team.xml',
    ],
    'assets': {
        'web.assets_backend': [
                 'crm_dashboard/static/src/js/crm_dashboard.js',
                 'crm_dashboard/static/src/xml/crm_dashboard.xml',
        ],
        "web.chartjs_lib": [
            '/web/static/lib/Chart/Chart.js',
            '/web/static/lib/chartjs-adapter-luxon/chartjs-adapter-luxon.js',
        ]
    }

}