# -*- coding: utf-8 -*-

from odoo import fields, models


class QualityMeasure(models.Model):
    """Model to create quality measure for product in specific stock move"""
    _name = 'quality.measure'
    _inherit = ['mail.thread']

    name = fields.Char('Name', required=True, tracking=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    type = fields.Selection([('quantity', 'Quantitative'),
                                      ('quality', 'Qualitative')],
                                  string='Test Type', default='quality', required=True, tracking=True)
    trigger_time = fields.Many2many('stock.picking.type', string='Trigger On', required=True)
    active = fields.Boolean('Active', default=True, tracking=True)
