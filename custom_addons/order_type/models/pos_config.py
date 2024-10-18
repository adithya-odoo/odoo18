# -*- coding: utf-8 -*-

from odoo import fields, models


class PosConfig(models.Model):
    """ To insert a  limit field inside the pos settings"""
    _inherit = 'pos.config'

    order_type_ids = fields.Many2many('order.type', string='Order Type')
    # test_field = fields.Char(string="test")

