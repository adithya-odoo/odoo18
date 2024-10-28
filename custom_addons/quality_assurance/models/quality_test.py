# -*- coding: utf-8 -*-

from odoo import api, fields, models


class QualityTest(models.Model):
    """This model contains quality tests assigned to specific user"""
    _name = 'quality.test'
    _inherit = ['mail.thread']

    quality_measure = fields.Many2one('quality.measure', string='Measure',
                                      index=True, ondelete='cascade', tracking=True)
    alert_id = fields.Many2one('quality.alert', string="Quality Alert",
                               tracking=True)
    name = fields.Char('Name', related="quality_measure.name", required=True)
    product_id = fields.Many2one('product.product', string='Product',
                                 related='alert_id.product_id')
    test_type = fields.Selection(related='quality_measure.type',
                                 string='Test Type', required=True,
                                 readonly=True)
    test_user_id = fields.Many2one('res.users', string='Assigned to',
                                   tracking=True)
    test_result = fields.Float(string='Result', tracking=True)
    test_result2 = fields.Selection([
         ('satisfied', 'Satisfied'),
        ('unsatisfied', 'Unsatisfied')], string='Result', tracking=True)
    test_status = fields.Selection(compute="_compute_status",
                                   selection=[('pass', 'Passed'),
                                              ('fail', 'Failed')],
                                   store=True, string='Status',
                                   tracking=True)

    @api.depends('test_result', 'test_result2')
    def _compute_status(self):
        """This function will compute the status"""
        for test in self:
            if test.test_result2 == 'satisfied':
                test.test_status = 'pass'
            else:
                test.test_status = 'fail'