from odoo import models

class IrUiMenu(models.Model):
    _inherit = "ir.ui.menu"

    def _visible_menu_ids(self, debug=False):
        res = super()._visible_menu_ids(debug=debug)
        company = self.env.company
        if not company.boolean_setting:
            menu = self.env.ref('practice_sales_and_contacts.menu_customer_wise_sales', raise_if_not_found=False)
            if menu:
                res = res - menu
        return res