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
from datetime import datetime

class eq_project_extension(models.Model):
    """
    this class is used to calculate the time fields that will be displayed in the kanban

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
        This overwrites the create method. give a project number automatically

        :param vals:
        :return:
        """

        seq = self.env['ir.sequence'].next_by_code('eq_project_number')
        vals['eq_project_number'] = seq
        return super(eq_project_extension, self).create(vals)


    def nummer_generator(self):
        """
        give a project number automatically, if not set
        :return:
        """
        if self.eq_project_number=="": # do not overwrite project nummer
            seq = self.env['ir.sequence'].next_by_code('eq_project_number')
            self.eq_project_number = seq
        else:
            pass




    #@api.onchange('eq_total_hours') #planned_hours
    def _calculated_total_time(self):
        """
            calculate the total time invested in the project
        :return:
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
        calculate the working time invested in the project
        :param self:
        :return:
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
        :param self:
        :return:
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










class eq_project_extension_2(models.Model):
        _inherit = 'account.analytic.line'
        eq_startdate = fields.Char(string='Start Date')
        eq_time_start = fields.Float(string='time start')
        name = fields.Text(string='Description', required=True)

        eq_counter = fields.Boolean(string='Counter')

        @api.onchange('project_id')
        def account_billiable(self):
            """
            ensures that the field eq_to_invoice_id  automatically recorded in the account.analytic.line
            :return:
            """
            for account in self:
               project_obj= self.env['project.project'].search([('id', '=', account.project_id.id)])

               for obj in  project_obj:
                   self.to_invoice = obj.eq_to_invoice_id







        @api.onchange('project_id')
        def set_time_onchange(self):

            eq_time_start = 0.0

            #
            # search hier im account.analytic.line where id = self.project_id dann for schleife
            check_existing_number = self.env['account.analytic.line'].search([('project_id', '=', self.project_id.id)])
            for  time  in check_existing_number:
                  if time.time_stop > eq_time_start:
                      eq_time_start= time.time_stop
            self.time_start = eq_time_start




        # @api.onchange('project_id')
        # def set_project_onchange(self):
        #
        #     check_existing_id = self.env['account.analytic.line'].search([('project_id', '=', self.project_id.id)])
        #     for id in check_existing_id:
        #         self.eq_counter = self.eq_counter + 1
        #
        #         if self.eq_counter >1 :
        #             self.project_id =




        @api.onchange('time_start')
        def set_time_start_onchange(self):



            if self.time_start > 23.59:
                # warning Message
                self.time_start = 0.0
               # raise Warning(_("Please enter a valid Hour"))

            else:
                pass


        @api.onchange('time_stop')
        def set_time_stop_onchange(self):

            if self.time_stop > 23.59:
                # warning Message
                self.time_stop = 0.0
                #raise Warning(_("Please enter a valid Hour"))

            else:
                pass




        # @api.onchange('project_id')
        # def set_time_onchange(self):
        #     # search hier im account.analytic.line where id = self.project_id dann for schleife
        #     pool = self.env['account.analytic.line']
        #     eq_item =0
        #     for ids in pool:
        #         if ids['project_id'] > eq_item:
        #             eq_item = ids['project_id']


















