from odoo import models, fields

class ResCompany(models.Model):
    _inherit = "res.company"

    boolean_setting = fields.Boolean(string="Boolean Settings")