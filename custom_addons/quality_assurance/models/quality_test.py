# -*- coding: utf-8 -*-

from odoo import api, fields, models

from odoo.exceptions import ValidationError

class QualityTest(models.Model):
    """This model contains quality tests assigned to specific user"""
    _name = 'quality.test'
    _inherit = ['mail.thread']

    quality_measure = fields.Many2one('quality.measure', string='Measure', ondelete='cascade', tracking=True)
    alert_id = fields.Many2one('quality.alert', string="Quality Alert",
                               tracking=True)
    name = fields.Char('Name', related="quality_measure.name", required=True)
    product_id = fields.Many2one('product.product', string='Product',
                                 related='alert_id.product_id')
    test_type = fields.Selection(related='quality_measure.type',
                                 string='Test Type', required=True,
                                 readonly=True)
    test_user_id = fields.Many2one('res.users', string='Assigned to', store=True, track_visibility='onchange')
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
        if self.test_type == 'quantity':
            self.test_result = 1
            quality_alert = self.env['quality.alert'].search([('id', '=', self.alert_id._origin.id)])
            move = self.env['stock.picking'].search([('id', '=', quality_alert.picking_id._origin.id)])
            for product in move.move_ids:
                if product.product_id.id == quality_alert.product_id.id:
                    if product.product_uom_qty < self.test_result:
                        raise ValidationError('Invalid number of product')
                    elif self.test_result2 == 'satisfied' and product.product_uom_qty == self.test_result:
                        self.test_status = 'pass'
                        product.quantity += self.test_result
                    elif self.test_result == 0:
                        raise ValidationError('Invalid number of product')
                    else:
                        self.test_status = 'fail'
        else:
            for test in self:
                if test.test_result2 == 'satisfied':
                    test.test_status = 'pass'
                else:
                    test.test_status = 'fail'