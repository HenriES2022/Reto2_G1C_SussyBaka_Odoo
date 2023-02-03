# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class Course(models.Model):
    _name = 'sussy_baka.course'

#   Fields

    name = fields.Char(required=True)
    description = fields.Text()
    start_date = fields.Date()
    private = fields.Boolean()
    visible = fields.Boolean()
    
#   Fields Relations
    
    teacher_id = fields.Many2one('res.users', string="Teacher")
    subject_id = fields.Many2one('sussy_baka.subject', string="Subject")
    post_id = fields.One2many('sussy_baka.post', 'course_id', string="Posts")
    student_id = fields.Many2many('res.users', string="Students")

    @api.constrains('star_date')
    def _check_date(self):
        for course in self:
            if course.start_date < 01/01/2000:
                raise ValidationError("Your record is to old")
    