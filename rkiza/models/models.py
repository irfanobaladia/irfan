# -*- coding: utf-8 -*-

# from odoo import models, fields, api

from odoo import models, fields, api, _
from odoo.exceptions import RedirectWarning, UserError, ValidationError


class Branch(models.Model):
    _name = 'rkiza.module'


    city_name = fields.Char(string='city Name')
    emp_name = fields.Char(string='employee Name')
    emp_number = fields.Integer('employee number')
    branch = fields.Selection(selection=[('riyadh', 'Riyadh'), ('onaizah', 'Onaizah')])
    customer = fields.Many2one("res.partner", string="Customer")
    state = fields.Selection([
        ('draft', 'To Submit'),
        ('hr', 'HR Approval'),
        ('ceo', 'CEO Approval'),
        ('finance', 'Finance Approval'),
        ('done', 'Done')], string='Status', copy=False, default='draft')
        

    def action_draft(self):
        self.write({'state': 'draft'})
        

    def action_ceo(self):
        self.write({'state': 'ceo'})
        

    def action_hr(self):
        self.write({'state': 'hr'})
        

    def action_finance(self):
        self.write({'state': 'finance'})
        

    def action_done(self):
        self.write({'state': 'done'})

