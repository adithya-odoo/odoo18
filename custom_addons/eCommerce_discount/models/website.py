# -*- coding: utf-8 -*-

from odoo import fields, models


class Website(models.Model):
    _inherit = 'website'

    default_discount = fields.Many2one('loyalty.rule', 'Default Discount')