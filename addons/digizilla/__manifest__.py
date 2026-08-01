{
    'name': 'Digizilla',
    'version': '19.0.1.0.0',
    'summary': 'Digizilla assessment module',
    'category': 'Custom',
    'depends': ['base', 'mail', 'sale'],
    'author': 'Roaa',
    'data': [
        'security/digizilla_groups.xml',
        'security/ir.model.access.csv',
        'views/digizilla_views.xml',
        'views/digizilla_menu.xml',
        'report/digizilla_report_templates.xml',
        'report/digizilla_report.xml',
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