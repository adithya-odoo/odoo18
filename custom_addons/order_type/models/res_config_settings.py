# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    """To insert field in settings"""
    _inherit = 'res.config.settings'

    pos_is_order_type = fields.Boolean(string='Order Type',
                                       related="pos_config_id.is_order_type",
                                       readonly=False)
    pos_order_type_ids = fields.Many2many(
        related="pos_config_id.order_type_ids", readonly=False)

    @api.onchange('pos_is_order_type')
    def onchange_pos_is_order_type(self):
        """To clear order_type_ids field in the pos.config
        the while disable the is_order_type in pos.config"""
        if not self.pos_is_order_type:
            self.pos_order_type_ids = False
