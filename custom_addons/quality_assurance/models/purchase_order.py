# -*- coding: utf-8 -*-

from odoo import models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        res = super().button_confirm()
        quality_assurance = self.env['quality.assurance'].search_read([('trigger_ids', '=', 1)])
        if self.env['quality.assurance'].search_read([('trigger_ids', '=', 1)]):
            if self.order_line.product_id.ids :
                print(self.order_line.product_id.ids)
                print(self.env['quality.assurance'].search_read([('trigger_ids', '=', 1)]))
        return  res
