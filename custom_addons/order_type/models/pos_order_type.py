# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PosOrderType(models.Model):
    _name = 'pos.order.type'
    _description = 'Pos Order Type'
    _inherit = ['pos.load.mixin']

    name = fields.Char(string="Order Type")

