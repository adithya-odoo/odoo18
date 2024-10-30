# -*- coding: utf-8 -*-

from odoo import api, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order"

    def _prepare_order_line_values(
            self, product_id, quantity, event_booth_pending_ids=False, registration_values=None,
            **kwargs
    ):
        """Add corresponding event to the SOline creation values (if booths are provided)."""
        values = super()._prepare_order_line_values(product_id, quantity, **kwargs)

        return values
