from odoo import models, fields, api

class KhachHang(models.Model):
    _name = 'khach_hang'
    _description = 'Bảng chứa thông tin khách hàng'
    _rec_name = 'name'
    _order = 'id asc, name asc'

    customer_id = fields.Char(string='Mã khách hàng', readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('khach_hang.customer_id'))
    name = fields.Char(string='Tên khách hàng', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Số điện thoại')
    address = fields.Text(string='Địa chỉ')
    
    customer_type = fields.Selection(
        [('individual', 'Cá nhân'), ('company', 'Doanh nghiệp')],
        string='Loại khách hàng', default='individual', required=True
    )
    company_name = fields.Char(string='Tên công ty')
    
    created_at = fields.Datetime(string='Ngày tạo', default=fields.Datetime.now, readonly=True)
    updated_at = fields.Datetime(string='Ngày cập nhật', default=fields.Datetime.now)
    
    @api.model
    def create(self, vals):
        vals['created_at'] = fields.Datetime.now()
        return super(KhachHang, self).create(vals)
    
    def write(self, vals):
        vals['updated_at'] = fields.Datetime.now()
        return super(KhachHang, self).write(vals)