# -*- coding: utf-8 -*-
{
    'name': "my_project_extension",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,
    'sequence': -1,
    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project','web'],
    'assets': {
        'web.assets_backend': [
            'my_project_extension/static/src/components/**/*.js',
            'my_project_extension/static/src/components/**/*.xml',
            'my_project_extension/static/src/components/**/*.scss',
        ],
    },

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/project_view.xml',
        'views/team_views.xml',
        'views/tasks_dashboard.xml',
        'data/record_rules.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
