from odoo import models,fields


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    hide_specification_page = fields.Boolean(string='Hide Specification Button', compute='_compute_hide_specification_button')

    def _compute_hide_specification_button(self):
        for record in self:
            record.hide_specification_page = False
            groups = self.env['product.access'].search([])
            for group in groups.groups:
                if group in self.env.user.groups_id:
                    if not groups.access_to_component:
                        record.hide_specification_page = True