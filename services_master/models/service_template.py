from odoo import models, fields, api


class ServiceMaster(models.Model):
    _name = 'service.master'
    
    name = fields.Char(required=True)
    service_package = fields.Float(required=True)
    unit_of_measure = fields.Many2one('uom.uom')
