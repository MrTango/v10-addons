# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo Addon, Open Source Management Solution
#    Copyright (C) 2014-now Equitania Software GmbH(<http://www.equitania.de>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import models, fields, api, _


class eq_purchase_order(models.Model):
    _inherit = 'purchase.order'

    eq_head_text = fields.Html('Head Text')
    notes = fields.Html('Terms and conditions')

    user_id = fields.Many2one('res.users', string="User", default=lambda self: self.env.user)

    # Report
    show_planned_date = fields.Boolean(string='Show Planned Date')
    use_calendar_week = fields.Boolean('Use Calendar Week for Planned Date [equitania]')

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """
        Override für Wechsel der Partner_ID: Übernahme der custom-Felder
        :return:
        """

        super(eq_purchase_order, self).onchange_partner_id()

        partner = self.partner_id
        if partner:
            self.partner_ref = partner.eq_foreign_ref_purchase


class eq_purchase_order_line(models.Model):
    _inherit = 'purchase.order.line'

    @api.multi
    def _get_planned_date(self):
        """
        Hilfsfunktion für Report für Ermittlung des Lieferdatums
        Aktuell wird Feld show_delivery_date der purchase_order nicht gesetzt -> Rückgabe immer false
        :return:
        """
        result = {}
        for purchase_line in self:
            if purchase_line.order_id.show_planned_date and purchase_line.date_planned:
                planned_date = datetime.strptime(purchase_line.date_planned, OE_DFORMAT)
                if purchase_line.order_id.partner_id.eq_planned_date_type_purchase:
                    if purchase_line.order_id.partner_id.eq_planned_date_type_purchase == 'cw':
                        result[purchase_line.id] = 'KW ' + planned_date.strftime('%V/%Y')
                    elif purchase_line.order_id.partner_id.eq_planned_date_type_purchase == 'date':
                        result[purchase_line.id] = planned_date.strftime('%d.%m.%Y')
                else:
                    if purchase_line.order_id.use_calendar_week:
                        result[purchase_line.id] = 'KW ' + planned_date.strftime('%V/%Y')
                    else:
                        result[purchase_line.id] = planned_date.strftime('%d.%m.%Y')
            else:
                result[purchase_line.id] = False
        return result

    get_planned_date = fields.Char(compute="_get_planned_date", string="Planned Date", methode=True, store=False)

class eq_purchase_configuration_address(models.TransientModel):
    _inherit = 'purchase.config.settings'
    # _inherit = _name

    def set_default_values(self):
        ir_values_obj = self.env['ir.values']

        ir_values_obj.set_default('purchase.order', 'show_planned_date', self.default_show_planned_date)
        ir_values_obj.set_default('purchase.order', 'use_calendar_week', self.default_use_calendar_week)

    def get_default_values(self, fields):
        ir_values_obj = self.env['ir.values']

        show_planned_date = ir_values_obj.get_default('purchase.order', 'show_planned_date')
        use_calendar_week = ir_values_obj.get_default('purchase.order', 'use_calendar_week')

        return {
            'default_show_planned_date': show_planned_date,
            'default_use_calendar_week': use_calendar_week,
        }


    default_show_planned_date = fields.Boolean(string='Show the Planned Date on the Purchase Order [equitania]',
                                               help='The planned date will be shown in the Purchase Order',
                                               default_model='purchase.order')
    default_use_calendar_week = fields.Boolean('Show Calendar Week for Planned Date [equitania]',
                                                help='The planned date will be shown as a calendar week',
                                                default_model='purchase.order')
