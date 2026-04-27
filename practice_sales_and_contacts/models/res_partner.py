from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    sales_count = fields.Integer(string="Sales Count", compute="_compute_sales_count")
    customer_code = fields.Char(string="Customer Code", readonly=True)

    def _compute_sales_count(self):
        for rec in self:
            rec.sales_count = self.env['sale.order'].search_count([
                ('partner_id', '=', rec.id)
            ])

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('customer_code'):
                vals['customer_code'] = self.env['ir.sequence'].next_by_code(
                    'res.partner.customer.code'
                )
        return super(ResPartner, self).create(vals)