# -*- coding: utf-8 -*-
{
    'name': "Persian Font",
    'summary': """Change Odoo Default Font To Vazir""",
    'author': "AliReza Nemati",
    'website': "https://pasargaddev.ir/",
    "category": "Localization/Iran",
    "version": "1.2.1",
    'depends': ['web'],
    'license': 'LGPL-3',
    'assets': {
        'web._assets_primary_variables': [
            'l10n_ir_fonts/static/src/scss/persianfont.scss',
        ],
        'web.assets_backend': [
            'l10n_ir_fonts/static/src/css/pos_style.css',
            'l10n_ir_fonts/static/src/css/web_style.css',
        ],
        'web.report_assets_common': [
            'l10n_ir_fonts/static/src/css/pdf_style.css',
        ],
        'web.report_assets_pdf': [
            'l10n_ir_fonts/static/src/css/pdf_style.css',
        ],
        'account_reports.assets_financial_report': [
            'l10n_ir_fonts/static/src/css/pdf_style.css',
        ],
    },
    "installable": True,
    "auto_install": False,
}
