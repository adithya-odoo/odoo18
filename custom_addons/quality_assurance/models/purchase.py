# -*- coding: utf-8 -*-

from odoo import models, _


class PurchaseOrder(models.Model):
    """To add functionality of generating quality alert from purchase order"""
    _inherit = "purchase.order"

    def _create_picking(self):
        """ To generate quality alert for if product_id and stock.move became
             same"""
        res = super()._create_picking()
        for products in self.order_line:
            if self.env['quality.measure'].search(
                    [('product_id', '=', products.product_id.id),
                     ('trigger_time', 'in', self.picking_type_id.id)]):
                self.env['quality.alert'].create({
                    'name': self.env['ir.sequence'].next_by_code(
                        'quality.reference') or _('New'),
                    'product_id': products.product_id.id,
                    'picking_id': self.picking_ids.id,
                    'origin': self.picking_ids.name,
                })
        return res
