# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class QualityAlert(models.Model):
    _name = 'quality.alert'
    _description = 'Quality alert'


    name = fields.Char('Reference', default=lambda self: _('New'),
                       copy=False,
                       readonly=True, tracking=True)
    source_id = fields.Many2one('stock.picking', 'source operation')

    @api.model_create_multi
    def create(self, vals_list):
        """ To create vehicle service form sequence """
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'quality.reference')
        return super().create(vals_list)
