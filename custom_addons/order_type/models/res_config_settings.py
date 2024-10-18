# -*- coding: utf-8 -*-

from odoo import fields, models,api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_order_type_ids = fields.Many2many('order.type', string="Order Type"
                                          ,related="pos_config_id.order_type_ids")
    # pos_test_field = fields.Char(related='pos_config_id.test_field',
    #                              string="test")

    # @api.depends('pos_test_field')
    # def compute_abc(self):
    #     for res_config in self:
    #         res_config.pos_order_type_ids = res_config.pos_config_id.order_type_ids


