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
from datetime import datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as OE_DFORMAT
import time
from odoo.exceptions import Warning


class eq_project_extension(models.Model):
    """
    Extension of project.project class
    Added our new fields to be able to save and calculate all important data like deadline, worked hours etc.
    """
    _inherit = 'project.project'

    eq_project_number = fields.Char('Number')
    eq_deadline = fields.Date (string='Deadline Date', compute='_deadline_date')
    eq_rest_hours = fields.Float(string='rest Time', compute='_calculated_rest_time')
    eq_total_hours = fields.Float(string=' total Time', compute='_calculated_total_time')
    eq_worked_hours = fields.Float(string='worked Time', compute='_calculated_worked_time')
    eq_time_start = fields.Float(string='Begin Hour')
    eq_time_stop = fields.Float(string='End Hour')

    @api.model
    def create(self, vals):
        """
        Create new record in project.project and return id of new created record back
        :param vals: All values that will be saved
        :return: ID of created record
        """
        seq = self.env['ir.sequence'].next_by_code('eq_project_number')
        vals['eq_project_number'] = seq
        return super(eq_project_extension, self).create(vals)

    def generate_number(self):
        """
        Generate project - just get next value from sequence and return it
        :return: New number from sequence
        """
        if self.eq_project_number=="":                                              # do not overwrite project nummer
            seq = self.env['ir.sequence'].next_by_code('eq_project_number')
            self.eq_project_number = seq
        else:
            pass

    def _deadline_date(self):
        """
        Simple forward definition of this function - it was defined by Kevin
        :return: Nothing yet
        """
        pass

    def _calculated_total_time(self):
        """
        Calculate total time of our project taks
        """
        eq_total_hour = 0.0
        for project in self:
            task_obj = self.env['project.task'].search([('project_id', '=', project.id)])
            for task in task_obj:
                if (task.stage_id.calculated_item) or len(task.stage_id) == 0:  # wenn stage_id only on state  (start & Umsetzung)
                    eq_total_hour = task.planned_hours + eq_total_hour
                else:
                    pass

            project.eq_total_hours = eq_total_hour
            eq_total_hour = 0.0

    def _calculated_rest_time(self):
        """
        Calculate the working time invested in the project
        """
        for project in self:
              eq_rest_hour = 0.0
              task_obj = self.env['project.task'].search([('project_id', '=', project.id)])
              for task in task_obj:
                  if (task.stage_id.calculated_item) or len(task.stage_id) == 0:  # wenn stage_id only on state  (start & Umsetzung)
                    eq_rest_hour = (task.planned_hours-((task.progress *  task.planned_hours)/100) ) + eq_rest_hour #progress was in percent
                  else:
                      pass

              project.eq_rest_hours = eq_rest_hour

    def _calculated_worked_time(self):
        """
        calculate the remaining work time to invest in the project
        """
        for project in self:
            task_obj = self.env['project.task'].search([('project_id', '=', project.id)])
            eq_worked_hour = 0.0
            for task in task_obj:
                if (task.stage_id.calculated_item) or len(task.stage_id) == 0:  # wenn stage_id only on state  (start & Umsetzung)
                    eq_worked_hour = ((task.progress *  task.planned_hours)/100 ) + eq_worked_hour #was in percent
                else:
                    pass

            project.eq_worked_hours = eq_worked_hour


class eq_account_analytic_line_project(models.Model):
    """
    Extension of account.analytic.line
    Changed logic on create, write and added new functions to be able to archive better useability
    """
    _inherit = 'account.analytic.line'

    MAX_POSSIBLE_HOURS = 24.00

    def invoice_cost_create(self, data=None):
        res = super(eq_account_analytic_line_project, self).invoice_cost_create(data)
        for obj in self:
            obj.write({'eq_storno_flag': False})
        return res

    def _get_project_from_context(self):
        """
        Small helper function - get project_id of last created record to be able to preset project that we used in last record
        :return: ID of last used project
        """
        objs = self.search([], order='id desc')
        if len(objs) > 0:
            obj = objs[0]
            project_id = obj.project_id
            return project_id

    @api.onchange('to_invoice','unit_amount')
    def _compute_time_invoice(self):
        for line in self:
            to_invoice = ((100 - line.to_invoice.factor) / 100) * line.unit_amount
            line.eq_time_invoice = to_invoice

    def _compute_proceed(self):

        for line in self:
            if line.eq_invoice_line_id:
                line.eq_proceed = line.eq_invoice_line_id.price_subtotal
            else:
                if len(line.invoice_id.invoice_line_ids) > 0:
                    invoice_line_id = self.env['account.invoice.line'].search([('invoice_id','=',line.invoice_id.id),('product_id','=',line.product_id.id),('eq_user_id','=',line.user_id.id),('quantity','=',-1 * line.unit_amount)])
                    if len(invoice_line_id) > 0:
                        line.eq_proceed = -1 * invoice_line_id[0].price_subtotal


    @api.onchange('project_id')
    def onchange_project_id(self):
        for line in self:
            user_id = line.env.context.get('user_id', self.env.user.id)
            project_obj = line.project_id
            if 'default_task_id' in self._context:
                task_id = self._context['default_task_id']
                task_obj = self.env['project.task'].browse(task_id)
            employee = self.env['hr.employee'].search([('user_id', '=', user_id)])
            if task_obj:
                if task_obj.eq_product_id.id:
                    line.product_id = task_obj.eq_product_id.id
                elif project_obj.eq_product_id.id:
                    line.product_id = project_obj.eq_product_id.id
                elif employee.product_id.id:
                    line.product_id = employee.product_id.id
                else:
                    ir_values_obj = self.env['ir.values']
                    product_id = ir_values_obj.get_default('project.task', 'default_project_product')
                    prod_obj = self.env['product.product'].search([('id', '=', product_id)])
                    if len(prod_obj) > 1:
                        prod_obj = prod_obj[0]
                    line.product_id = prod_obj.id
            elif project_obj:
                if project_obj.eq_product_id.id:
                    line.product_id = project_obj.eq_product_id
                elif employee.product_id.id:
                    line.product_id = employee.product_id
                else:
                    ir_values_obj = self.env['ir.values']
                    product_id = ir_values_obj.get_default('project.task', 'default_project_product')
                    prod_obj = self.env['product.product'].search([('id', '=', product_id)])
                    if len(prod_obj) > 1:
                        prod_obj = prod_obj[0]
                        line.product_id = prod_obj
            else:
                if employee.product_id.id:
                    line.product_id = employee.product_id
                else:
                    ir_values_obj = self.env['ir.values']
                    product_id = ir_values_obj.get_default('project.task', 'default_project_product')
                    prod_obj = self.env['product.product'].search([('id', '=', product_id)])
                    if len(prod_obj) > 1:
                        prod_obj = prod_obj[0]
                    line.product_id = prod_obj



    eq_startdate = fields.Char(string='Start Date')
    eq_time_start = fields.Float(string='time start')
    name = fields.Text(string='Description', required=True)
    project_id = fields.Many2one('project.project', 'Project', domain=[('allow_timesheets', '=', True)], default=_get_project_from_context)
    sheet_id = fields.Many2one('hr_timesheet_sheet.sheet', compute='_compute_sheet', string='Sheet', store=True)
    eq_storno_flag = fields.Boolean(string='storniert', default=False)
    eq_time_invoice = fields.Float(string="Time to Invoice", compute=_compute_time_invoice)

    eq_proceed = fields.Float(string='Proceed', compute=_compute_proceed)

    issue_id = fields.Many2one('project.issue', 'Issue', copy=True, domain="[('project_id', '=', project_id)]")
    task_id = fields.Many2one('project.task', 'Task', copy=True, domain="[('project_id', '=', project_id)]")

    @api.model
    def create(self, vals):
        """
        Create new record in account.analytic.line and return id of new created record back
        :param vals: All values that will be saved
        :return: ID of created record
        """
        if 'time_start' in vals:
            if vals['time_start'] >= self.MAX_POSSIBLE_HOURS:
                raise Warning(_("Please enter a valid Hour"))
        if 'time_stop' in vals:
            if vals['time_stop'] >= self.MAX_POSSIBLE_HOURS:
                raise Warning(_("Please enter a valid Hour"))

        vals['eq_storno_flag'] = False

        res = super(eq_account_analytic_line_project,self).create(vals)
        if 'amount' in vals:
            if vals['amount'] < 0:
                res.write({'unit_amount': -1 * res.unit_amount})
        return res

    @api.multi
    def write(self, vals):
        """
        Update an existing record in account.analytic.line and return id of updated record back
        :param vals: All values that will be saved
        :return: ID of updated record
        """
        if 'time_start' in vals:
            if vals['time_start'] >= self.MAX_POSSIBLE_HOURS:
                raise Warning(_("Please enter a valid Hour"))
        if 'time_stop' in vals:
            if vals['time_stop'] >= self.MAX_POSSIBLE_HOURS:
                raise Warning(_("Please enter a valid Hour"))

        return super(eq_account_analytic_line_project, self).write(vals)

    @api.onchange('project_id')
    def set_time_onchange(self):
        """
        OnChangeHandler for project_id - recalculate and set time
        """
        eq_time_start = 0.0
        eq_startdate = time.strftime("%Y-%m-%d")            # set today's date as default date

        if self.project_id.id == False:
            pass
        else:
            account_analytic_objs = self.env['account.analytic.line'].search([('project_id', '=', self.project_id.id),('time_start','!=',False),('time_stop','!=',False)],order='date desc,time_stop desc')
            project_objs = self.env['project.project'].search([('id', '=', self.project_id.id)])
            if len(project_objs) > 0:
                project_obj = project_objs[0]
                self.to_invoice = project_obj.eq_to_invoice_id

            if len(account_analytic_objs) > 0:
                account_analytic_obj = account_analytic_objs[0]
                if account_analytic_obj.time_stop > eq_time_start:
                    eq_time_start = account_analytic_obj.time_stop
                if (account_analytic_obj.date) > eq_startdate:
                    eq_startdate = account_analytic_obj.date

            if eq_time_start > 23.97:
                eq_time_start = 0.00
                last_date = account_analytic_obj.date
                date = datetime.strptime(last_date,'%Y-%m-%d')
                self.date = date + timedelta(days=1)
            else:
                self.date = eq_startdate

            self.time_start = eq_time_start

        # Show the issues from the selected project
        # res = {}
        # if self.project_id:
        #     project = self.project_id
        #     if project != self.issue_id.project_id:
        #         self.issue_id = False
        #     res['domain'] = {'issue_id': [('project_id', '=', project.id)]}
        # else:
        #     res['domain'] = {'issue_id': []}
        # return res