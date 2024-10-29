from lxml import etree

from odoo import models, api, fields
from odoo.exceptions import AccessError


class ProductAccess(models.Model):
    _name = 'product.access'

    name = fields.Char(string='Name', compute='_compute_name')

    product_categories_for_access = fields.Many2many(
        'product.category',
        string='Product Categories for Access Restriction',
        config_parameter='hk_access_for_mixtures.product_categories_for_access'
    )

    groups = fields.Many2one(
        'res.groups',
        string='Groups',
        config_parameter='hk_access_for_mixtures.groups'
    )

    access_to_component = fields.Boolean(string='Access to Component')

    def _compute_name(self):
        for record in self:
            record.name = f'{record.product_categories_for_access.name} - {record.groups.name}'
