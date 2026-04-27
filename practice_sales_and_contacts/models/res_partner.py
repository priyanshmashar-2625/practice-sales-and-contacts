from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    sale_order_count = fields.Integer(string="Sale Order Count", compute="_compute_sale_order_count")

    def _compute_sale_order_count(self):
        for rec in self:
            rec.sale_order_count = self.env['sale.order'].search_count([
                ('partner_id', '=', rec.id)
            ])