# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class custom_default_header(models.Model):
#     _name = 'custom_default_header.custom_default_header'
#     _description = 'custom_default_header.custom_default_header'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
