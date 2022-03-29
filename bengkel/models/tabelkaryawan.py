from odoo import api, fields, models


class TabelKaryawan(models.Model):
    _name = 'tabel.karyawan'
    _description = 'Tabel para Karyawan Bengkel'

    nomor = fields.Integer(string='No')
    noinduk = fields.Char(string='Nomor Induk')
    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgllahir = fields.Date(string='Tanggal Lahir')
    tglgabung = fields.Date(string='Tanggal Bergabung')

    
    
    
    
    
    
