# -*- coding: utf-8 -*-

from odoo import fields, models,api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_order_type_ids = fields.Many2many(string="Order Type"
                                          ,related="pos_config_id.order_type_ids", compute='compute_abc', readonly=False)
    # pos_is_order_type = fields.Boolean(related='pos_config_id.is_order_type',
    #                                    string='Order Type',
    #                                    readonly=False)

    @api.depends('pos_order_type_ids')
    def compute_abc(self):
        print("gggggg")
        for res_config in self:
            res_config.pos_order_type_ids = res_config.pos_config_id.order_type_ids


