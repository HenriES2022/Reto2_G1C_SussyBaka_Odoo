#The teacher class for the model

from odoo import models, fields, api

class teacher(models.Model):
    #The name of the model
    _name='sussy_baka.teacher'
    #The name of the teacher
    name= fields.Char(string="Name:", required=True, 
        help="The name of the teacher")
    
    #The subjects where the teacher is specialized
    specializedSubjects = fields.Many2many('sussy_baka.subject', string="Subject:")
    
    #The courses where the teacher teaches
    teachingCourses = fields.One2many('sussy_baka.course', string="Course:", 
        help="The course where the teacher teaches", ondelete='set null')