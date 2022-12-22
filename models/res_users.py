# The class for the extension of res.users

from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'
    
    #A boolean field to know if the user is a teacher
    isTeacher = fields.Boolean(string="Is teacher:", help="If the user is a teacher checked, else not checked")
    
    #A boolean field to know if the user is a student
    isStudent = fields.Boolean(string="Is studend", help="If the user is a studend checked, else not checked")

    #A One2many field with comment
    coments = fields.One2many('sussy_baka.comment', string="Coments:",
       help="The comments of the user", ondelete="cascade")
       
    #A Many2many field with subject
    subject_ids = fields.Many2many('sussy_baka.subject', string="Subject_ids:", help="The subject ids where the teacher is specialized")
       
    #A One2many field with course. teaching courses relation between a teacher and a course
    teaching_courses = fields.One2many('sussy_baka.course', string="Teaching courses:", help="The courses that the teacher is teaching")
    
    #A Many2many field with course. studying courses relation between a student and a course
    studying_courses = fields.Many2many('sussy_baka.course', string="Studying courses:", help="The courses that the student is studying")
    