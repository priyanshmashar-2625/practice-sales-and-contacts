from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    boolean_setting = fields.Boolean(
        string="Boolean Settings",
        related='company_id.boolean_setting',
        readonly=False
    )