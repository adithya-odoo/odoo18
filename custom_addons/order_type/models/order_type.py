# -*- coding: utf-8 -*-

from odoo import models, fields


class OrderType(models.Model):
    _name = 'order.type'
    _description = 'Order Type'

    name = fields.Char(string="Order Type")

