from lxml import etree

from odoo import models, api, fields
from odoo.exceptions import AccessError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    hide_specification_button = fields.Boolean(string='Hide Specification Button', compute='_compute_hide_specification_button')

    def write(self, vals):
        # Перевіряємо, чи користувач у групі з обмеженим доступом
        groups = self.env['product.access'].search([])
        for group in groups.groups:
            if group in self.env.user.groups_id:
                for product in self:
                    if product.categ_id.id in groups.product_categories_for_access.ids:
                        raise AccessError("Ви не маєте права редагувати продукти в цій категорії.")
        return super(ProductTemplate, self).write(vals)

    def _compute_hide_specification_button(self):
        for record in self:
            record.hide_specification_button = False
            groups = self.env['product.access'].search([])
            for group in groups.groups:
                if group in self.env.user.groups_id:
                    if record.categ_id.id in groups.product_categories_for_access.ids:
                        record.hide_specification_button = True
                        break