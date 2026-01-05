from odoo import models, fields, api


class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Bảng chứa thông tin công việc'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
