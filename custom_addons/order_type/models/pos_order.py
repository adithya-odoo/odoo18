# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PosOrder(models.Model):
    """to add a field in pos"""
    _inherit = 'pos.order'

    order_type = fields.Char('Order Type', compute='_compute_field', store=True)

    @api.depends('name')
    def _compute_field(self):
        print("hello,", self)
        print(self.search_read([]))
