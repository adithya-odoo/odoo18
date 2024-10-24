# -*- coding: utf-8 -*-

from odoo import api, fields, models


class QualityTrigger(models.Model):
    _name = 'quality.trigger'
    _description = 'Quality trigger'

    managing_id = fields.Many2one('quality.assurance')
    operation_type_id = fields.Many2one('stock.picking.type', 'Type name')
    warehouse_id = fields.Many2one('stock.warehouse', 'Warehouse')

