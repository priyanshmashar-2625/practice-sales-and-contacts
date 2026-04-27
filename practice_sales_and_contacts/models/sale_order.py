from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    total_line_qty = fields.Float(string="Total Quantity", compute="_compute_total_line_qty", store=True)

    @api.depends('order_line.product_uom_qty', 'order_line')
    def _compute_total_line_qty(self):
        for rec in self:
            # _logger.info(">>>>>>>>>>>>>>>>>>>>>>%s",rec.read())
            rec.total_line_qty = sum(line.product_uom_qty for line in rec.order_line)