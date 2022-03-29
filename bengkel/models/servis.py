from odoo import api, fields, models


class BengkelServis(models.Model):
    _name = 'bengkel.servis'
    _description = 'Servis Kendaraan'

    nomor = fields.Integer(string='No')
    kode = fields.Char(string='Kode SKU')
    name = fields.Char(string='Layanan Servis')
    stok = fields.Integer(string='Maintenance')
    harga = fields.Integer(string='Biaya')

