# -*- coding: utf-8 -*-

from odoo import api, models


class PosSession(models.Model):
    """To write a function to load order type data to the pos"""
    _inherit = 'pos.session'

    @api.model
    def _load_pos_data_models(self, config_id):
        """load the data to the pos.config.models"""
        data = super()._load_pos_data_models(config_id)
        data += ['pos.order.type']
        return data
