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
            measure = self.env['quality.measure'].search(
                [('product_id', '=', products.product_id.id),
                 ('trigger_time', 'in', self.picking_type_id.id)])
            if measure:
                self.env['quality.alert'].create({
                    'name': self.env['ir.sequence'].next_by_code(
                        'quality.reference') or _('New'),
                    'product_id': products.product_id.id,
                    'picking_id': self.picking_ids.id,
                    'origin': self.picking_ids.name,
                })
                # if measure.type == 'quantity':
                #     move = self.env['stock.picking'].search([('id', '=', self.picking_ids.id)])
                #     for product in move.move_ids:
                #         if product.product_id.id == measure.product_id.id:
                #             product.quantity = 0
        return res
