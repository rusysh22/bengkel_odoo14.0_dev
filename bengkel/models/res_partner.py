from email.policy import default
from odoo import api, fields, models


class Customer(models.Model):
    _inherit = 'res.partner'

    is_pegawainya = fields.Boolean(string='Customer Baru',
    default=False
    )
    is_customernya = fields.Boolean(string='Member', default=False)
    

