from odoo import api, fields, models
from odoo.exceptions import ValidationError



class Order(models.Model):
    _name = 'bengkel.order'
    _description = 'New Description'

    servisdetail_ids = fields.One2many(
        comodel_name='bengkel.servisdetail', 
        inverse_name='orderk_id', 
        string='Servis')
    
    sparepartdetail_ids = fields.One2many(
        comodel_name='bengkel.sparepartdetail', 
        inverse_name='orders_id',
        string='Sparepart')
    
    
    name = fields.Char(string='Kode Order', required=True)
    tanggal_datang = fields.Datetime(string ='Tanggal Kedatangan',default=fields.Datetime.now())
    tanggal_kirim = fields.Date(string='Tanggal Pengambilan', default=fields.Date.today())
    pemesan = fields.Many2one(
        comodel_name='res.partner', 
        string='Pemesan', 
        domain=[('is_customernya','=', True)],store=True)
        
    
    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    
    @api.depends('servisdetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['bengkel.servisdetail'].search([('orderk_id', '=', record.id)]).mapped('harga'))
            b = sum(self.env['bengkel.sparepartdetail'].search([('orders_id', '=', record.id)]).mapped('harga'))
            record.total = a + b
    
    sudah_ambil = fields.Boolean(string='Siap Ambil', default=False)

class ServisDetail(models.Model):
    _name = 'bengkel.servisdetail'
    _description = 'New Description'

    orderk_id = fields.Many2one(comodel_name='bengkel.order', string='Order Servis')
    servis_id = fields.Many2one(
        comodel_name='bengkel.servis', 
        string='Servis', 
        domain=[('stok','>','1')])
    
         
    name = fields.Char(string='Nama')
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    qty = fields.Integer(string='Quantity')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Biaya')

    @api.constrains('qty')
    def _check_stok(self):
        for record in self:
            bahan = self.env['bengkel.servis'].search([('stok', '<',record.qty),('id', '=',record.id)])
            if bahan:
                raise ValidationError("Stok sparepart yang dipilih tidak cukup")
    
    @api.depends('servis_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.servis_id.harga
    
    
    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
           record.harga = record.harga_satuan * record.qty
           
    @api.model
    def create(self,vals):
        record = super(ServisDetail, self).create(vals) 
        if record.qty:
            self.env['bengkel.servis'].search([('id','=',record.servis_id.id)])
            return record


            
class SparepartDetail(models.Model):
    _name = 'bengkel.sparepartdetail'
    _description = 'New Description'
    
    orders_id = fields.Many2one(comodel_name='bengkel.order', string='Order Sparepart')
    sparepart_id = fields.Many2one(
        comodel_name='bengkel.sparepart', 
        string='Sparepart',
        domain=[('stok','>','1')])
    
    name = fields.Char(string='Name')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga')
    
    @api.depends('sparepart_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.sparepart_id.harga
    
    qty = fields.Integer(string='Quantity')
    
    @api.constrains('qty')
    def _check_stok(self):
        for record in self:
            bahan = self.env['bengkel.sparepart'].search([('stok', '<',record.qty),('id', '=',record.id)])
            if bahan:
                raise ValidationError("Stok sparepart yang dipilih tidak cukup")
    
    harga = fields.Integer(compute='_compute_harga', string='harga')
    
    @api.depends('harga_satuan','qty')
    def _compute_harga(self):
        for record in self:
               record.harga = record.harga_satuan * record.qty
               
    
    @api.model
    def create(self,vals):
        record = super(SparepartDetail, self).create(vals) 
        if record.qty:
            self.env['bengkel.sparepart'].search([('id','=',record.sparepart_id.id)])
            return record
    