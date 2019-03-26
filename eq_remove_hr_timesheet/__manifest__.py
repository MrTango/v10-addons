# -*- coding: utf-8 -*-
# Copyright Equitania Software GmbH - Germany - https://www.equitania.de
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Equitania Remove HR Timesheet',
    'license': 'AGPL-3',
    'version': '1.0.0',
    'description': """
        Equitania Remove HR Timesheet
    """,
    'author': 'Equitania Software GmbH',
    'website': 'www.myodoo.de',
    'depends': ['base_setup','hr_timesheet'],
    'category' : 'General Improvements',
    'summary': 'This module makes the HR Timesheet menuitem invisible',

    'data': [
        "views/templates.xml",

    ],
    'demo': [],
    'css': ['base.css'],
    'installable': True,
    'auto_install': False,
}
