# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import api, fields, models, _


class QualityAlert(models.Model):
    """This model is used to generate quality alert"""
    _name = 'quality.alert'
    _inherit = ['mail.thread']

    name = fields.Char('Name', required=True)
    date = fields.Datetime(string='Date', default=datetime.now(),
                           tracking=True)
    product_id = fields.Many2one('product.product', string='Product')
    picking_id = fields.Many2one('stock.picking', string='Source Operation')
    origin = fields.Char(string='Source Document', readonly=True)
    user_id = fields.Many2one('res.users', string='Created by',
                              default=lambda self: self.env.user.id)
    tests = fields.One2many('quality.test', 'alert_id', string="Tests")
    final_status = fields.Selection(compute="_compute_status",
                                    selection=[('wait', 'Waiting'),
                                               ('pass', 'Passed'),
                                               ('fail', 'Failed')],
                                    store=True, string='Status',
                                    default='fail', tracking=True)

    def generate_tests(self):
        """this functon is call when click the generate test button"""
        for measure in self.env['quality.measure'].search(
                       [('product_id', '=', self.product_id.id),
                        ('trigger_time', 'in', self.picking_id.picking_type_id.id)]):
            self.env['quality.test'].create({'quality_measure': measure.id,
                                             'alert_id': self.id})

    @api.depends('tests', 'tests.test_status')
    def _compute_status(self):
        """This function will compute the status"""
        for alert in self:
            failed_tests = [test for test in alert.tests if
                            test.test_status == 'fail']
            if not alert.tests:
                alert.final_status = 'wait'
            elif failed_tests:
                alert.final_status = 'fail'
            else:
                alert.final_status = 'pass'