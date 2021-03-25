from odoo import models, fields, api

class ProductCountryOfOrigin(models.Model):
    _inherit = "product.template"

    origin_country_id = fields.Many2one("res.country", "Country of Origin", help="Made in ...")
    purchase_country_id = fields.Many2one("res.country", "Country of Purchase", help="Purchased from ...")
    category_name = fields.Char(related='categ_id.name')
    service_category = fields.Many2one('service.master')

    @api.onchange('service_category', 'type')
    def fetch_cost_uom_of_service(self):
        if self.type == "service":
            self.list_price = self.service_category.service_package
            self.uom_id = self.service_category.unit_of_measure
        else:
            self.list_price = 0.0
            self.uom_id = ''


