from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    variant_count = fields.Integer(
        string="Variant Count",
        compute="_compute_variant_count",
        store=True
    )

    @api.depends('product_variant_ids')
    def _compute_variant_count(self):
        for rec in self:
            rec.variant_count = len(rec.product_variant_ids)