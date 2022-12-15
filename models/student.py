#This is the student class for the model

from odoo import models, fields, api

class student(models.Model):
    #The name of the model
    _name = 'sussy_baka.student'
    #name, because of the hierarchy, dont know how to put
    
    studyingCourses = fields.Many2many('sussy_baka.course', string="Course:")