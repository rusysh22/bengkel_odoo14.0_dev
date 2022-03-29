from odoo import api, fields, models


class BengkelSparepart(models.Model):
    _name = 'bengkel.sparepart'
    _description = 'Sparepart Kendaraan'

    nomor = fields.Integer(string='No')
    kode = fields.Char(string='Kode SKU')
    name = fields.Char(string='Nama Barang')
    stok = fields.Integer(string='Stok Barang')
    harga = fields.Integer(string='Harga Barang')


