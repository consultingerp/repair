# -*- coding: utf-8 -*-
{
    'name': "custom_report",

    'summary': """
       Permite Agregar Reporte Personalizado """,

    'description': """
        Permite Agregar Reporte Personalizado
    """,


    'author': "ITConsulting ",
    'website': "https://itcni.odoo.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','fleet_repair_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}