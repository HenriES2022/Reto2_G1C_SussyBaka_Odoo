from odoo import models, fields, api

#The subject class for the 
class Subject(models.Model):
    #The name of the model
    _name ='sussy_baka.subject'
    #The name of the subject
    name = fields.Char(string="Name:", required=True,
        help="Name of the subject")
    #The century of the creation of the subject
    century = fields.Char(string="Century:", required=True, 
        help="The century of creation of the subject")
    #The level of dificulty of the subject
    level = fields.Char(string="Level:", required=True, 
        help="The level of the subject")
    #The courses where the subject is going to be teached
    course_ids = fields.One2many('sussy_baka.course', string="Courses:",
        help="The courses where the subject is going to be teached", ondeldete='set null')
    
    #The teachers that are specialized in this subject
    teachers_ids = fields.Many2many('sussy_baka.teacher', string="teachers")
    