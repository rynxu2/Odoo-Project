# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class quan_ly_cong_viec(models.Model):
#     _name = 'quan_ly_cong_viec.quan_ly_cong_viec'
#     _description = 'quan_ly_cong_viec.quan_ly_cong_viec'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
