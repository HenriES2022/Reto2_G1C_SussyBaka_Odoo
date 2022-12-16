# The class for the extension of res.users

from odoo import models, fields, api

class res_users(models.Model):
    _inherit = 'res.users'
    
    #A boolean field to know if the user is a teacher
    isTeacher = fields.Boolean(string="Is teacher:", help="If the user is a teacher checked, else not checked")
    
    #A boolean field to know if the user is a student
    isStudent = fields.Boolean(string="Is studend", help="If the user is a studend checked, else not checked")

    #A One2many field with comment
    coments = fields.One2many('sussy_baka.comment', string="Coments:",
       help="The comments of the user", ondelete="cascade")
       
    #A One2many field with course
    teaching_courses = fields.One2many('sussy_baka.course', string="Teaching courses:", help="The courses that the teacher is teaching")