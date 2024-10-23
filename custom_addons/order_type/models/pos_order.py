# -*- coding: utf-8 -*-

from odoo import fields, models, api


class PosOrder(models.Model):
    """to add a field in pos"""
    _inherit = 'pos.order'

    order_type_id = fields.Many2one(comodel_name='pos.order.type' ,string='Order Type')
