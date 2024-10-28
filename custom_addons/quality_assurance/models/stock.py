# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

from odoo.exceptions import ValidationError



class StockPicking(models.Model):
    _inherit = "stock.picking"

    alert_count = fields.Integer(compute='_compute_alert',
                                 string='Quality Alerts', default=0)
    alert_ids = fields.Many2many('quality.alert', compute='_compute_alert',
                                 string='Quality Alerts', copy=False)

    @api.depends('move_ids')
    def _compute_alert(self):
        '''This function computes the number of
        quality alerts generated from given picking'''
        self.alert_ids = self.env['quality.alert'].search(
                               [('picking_id', '=', self.id)])
        self.alert_count = len(self.alert_ids)

    def quality_alert_action(self):
        '''This function return to the quality alert genererated to the
           corresponding stock  picking.'''
        print(self.id)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'quality.alert',
            'name': 'Quality Alerts',
            'views': [(False, 'list'),(False, 'form')],
            'domain': [('picking_id', '=', self.id)],
            'context': "{'create': False}",
        }

    def button_validate(self):
        '''This function will generate validation error if quality alert is
           failed or in waiting status'''
        res = super().button_validate()
        print(self.move_ids.product_id)
        for line in self.move_ids:
            for alert in self.env['quality.alert'].search(
                [('picking_id', '=', self.id),
                 ('product_id', '=', line.product_id.id)]):
                if alert.final_status == 'wait':
                    raise ValidationError('There are items still in quality test')
                if alert.final_status == 'fail':
                    raise ValidationError('There are items failed in quality test')
        return res