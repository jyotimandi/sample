from odoo import models, fields, api

class BillOfMaterials(models.Model):
    _inherit = 'mrp.bom'

    marble_trading = fields.Boolean(string="BOM On Marble Trading Product Category", default=True, help="if check box is ticket, then bill of materials can can create for Marble trading product categories")
