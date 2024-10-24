# -*- coding: utf-8 -*-

from odoo import fields, models


class PosOrder(models.Model):
    """to add a field in pos.order"""
    _inherit = 'pos.order'

    order_type_id = fields.Many2one(comodel_name='pos.order.type',
                                    string='Order Type')
