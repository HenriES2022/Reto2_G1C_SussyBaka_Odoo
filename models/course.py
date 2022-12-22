# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'sussy_baka.course'

#   Fields

    name = fields.Char(required=True)
    description = fields.Text()
    start_date = fields.Date()
    private = fields.Boolean()
    visible = fields.Boolean()
    
#   Fields Relations
    
    teacher_id = fields.Many2one('sussy_baka.teacher', string="Teacher")
    subject_id = fields.Many2one('sussy_baka.subject', string="Subject")
    post_id = fields.One2many('sussy_baka.post', 'post_ids', string="Posts")
    student_id = fields.Many2many('sussy_baka.student', string="student_ids")

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
