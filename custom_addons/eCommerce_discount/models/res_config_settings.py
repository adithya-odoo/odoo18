# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    website_default_discount = fields.Many2one(related='website_id.default_discount' , string='Default Discount', readonly=False)
