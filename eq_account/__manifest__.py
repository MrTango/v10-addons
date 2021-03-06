# -*- coding: utf-8 -*-
# Copyright 2014-now Equitania Software GmbH - Pforzheim - Germany
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Equitania Finanzen",
    'license': 'AGPL-3',
    'version': '1.0.76',
    'category': 'account',
    'description': """Extensions for account""",
    'author': 'Equitania Software GmbH',
    'summary': 'Account Extension',
    'website': 'www.myodoo.de',
    "depends" : ['base', 'base_setup', 'account','stock','eq_base_report','eq_sale_stock'],
    'data': [
            'views/account_invoice_view.xml',
            'views/report_invoice.xml',
            'views/report_overdue.xml',
            'views/eq_account_payment_term.xml',
            'security/ir.model.access.csv',
             ],
    "active": False,
    "installable": True
}
