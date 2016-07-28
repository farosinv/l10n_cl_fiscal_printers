# -*- coding: utf-8 -*-
{
    'name': "l10n_cl_fiscal_printers",

    'summary': """
        Módulo para registrar impresoras fiscales por compañía
        """,

    'description': """
        Permite el registro en el sistema de las impresoras fiscales 
        pertenecientes a cada empresa y algunas configuraciones básicas.
    """,

    'author': "Faros Inversiones Ltda.",
    'website': "http://www.farosinv.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}