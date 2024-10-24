# -*- coding: utf-8 -*-

from odoo import api, fields, models


class QualityAssurance(models.Model):
    _name = 'quality.assurance'
    _description = 'Quality Assurance module'

    name = fields.Char('Test')
    product_id = fields.Many2one('product.product', 'Product name')
    trigger_ids = fields.One2many('quality.trigger', 'managing_id',
                                  'Trigger on')

