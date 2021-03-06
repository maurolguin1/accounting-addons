# -*- coding: utf-8 -*-
# Copyright© 2017 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Account Move Line Report - Operating Unit Extension',
    'version': '8.0.0.0.1',
    'license': 'AGPL-3',
    'author': 'ICTSTUDIO, André Schenkels',
    'category': 'Accounting & Finance',
    'depends': [
        'account_move_line_report',
        'account_operating_unit'
        ],
    'data': [
        'report/account_move_line_report.xml',
        ],
    'installable': True,
}
