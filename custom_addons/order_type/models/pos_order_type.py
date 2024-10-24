# -*- coding: utf-8 -*-

from odoo import fields, models


class PosOrderType(models.Model):
    """Model to set the order type in the pos"""
    _name = 'pos.order.type'
    _description = 'Pos Order Type'
    _inherit = ['pos.load.mixin']

    name = fields.Char(string="Order Type")

