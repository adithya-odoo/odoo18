# -*- coding: utf-8 -*-
from email.policy import default

from odoo import fields, models, api


class PosConfig(models.Model):
    """ To insert a  limit field inside the pos settings"""
    _inherit = 'pos.config'

    order_type_ids = fields.Many2many('order.type', string='Order Type')
    # is_order_type = fields.Boolean(string='Order Type')



