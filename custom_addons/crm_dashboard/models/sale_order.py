# -*- coding: utf-8 -*-

from odoo import models


class SaleOrder(models.Model):
    """ To change the stage of crm.lead to the stage that given inside the sales
        team"""
    _inherit = 'sale.order'

    def action_confirm(self):
        """To change the stage of crm.lead to the stage that given inside the
           sales team"""
        res = super().action_confirm()
        if self.opportunity_id and self.opportunity_id.team_id.crm_stage_id:
            if  self.opportunity_id.stage_id != self.opportunity_id.team_id.crm_stage_id:
                self.opportunity_id.stage_id = self.opportunity_id.team_id.crm_stage_id
        return res