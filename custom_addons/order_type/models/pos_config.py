# -*- coding: utf-8 -*-

from odoo import fields, models


class PosConfig(models.Model):
    """ To insert field inside the pos settings"""
    _inherit = 'pos.config'

    is_order_type = fields.Boolean(string='Order Type')
    order_type_ids = fields.Many2many('pos.order.type', string='Order Type', help='The different order of this point of sale.')


