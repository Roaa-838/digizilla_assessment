{
    'name': 'Digizilla',
    'version': '19.0.1.0.0',
    'summary': 'Digizilla assessment module',
    'category': 'Custom',
    'author': 'Roaa',
    'depends': ['base', 'mail', 'sale'],
    'data': [
        'security/digizilla_groups.xml',
        'security/ir.model.access.csv',
        'report/digizilla_report_templates.xml',
        'report/digizilla_report.xml',
        'views/digizilla_views.xml',
        'views/digizilla_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'digizilla/static/src/js/digizilla_form.js',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}