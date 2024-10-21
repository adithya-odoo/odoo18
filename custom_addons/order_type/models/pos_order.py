# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PosOrder(models.Model):
    """to add a field in pos"""
    _inherit = 'pos.order'

    order_type = fields.Char('Order Type')
