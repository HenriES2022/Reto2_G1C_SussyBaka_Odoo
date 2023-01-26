from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime
import re

#The subject class for the 
class Subject(models.Model):
    #The name of the model
    _name ='sussy_baka.subject'
    #The name of the subject
    name = fields.Char(string="Name", required=True,
        help="Name of the subject")
    #The century of the creation of the subject
    century = fields.Char(string="Century", required=True, 
        help="The century of creation of the subject")
    #The level of dificulty of the subject
    level = fields.Char(string="Level", required=True, 
        help="The level of the subject")
    #The courses where the subject is going to be teached
    course_ids = fields.One2many('sussy_baka.course', 'subject_id',string="Courses",
        help="The courses where the subject is going to be teached", ondeldete='set null')
    
    #The teachers that are specialized in this subject
    teachers_ids = fields.Many2many('res.users', string="teachers")
    
    #Validates that century field can only contains roman characters
    @api.constrains('century')
    def _check_century_only_roman_characters(self):
        if not re.match("^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", self.century):
            raise ValidationError("Century field only can have roman characters and yo have %s: " % self.century)

    #todo validates that introduced century is not bigger than the actual
    @api.constrains('century')
    def _check_century_is_not_bigger_than_actual(self):
        current_year = datetime.now().year
        current_century = None
        
        if current_year % 100 != 0
            current_century = (current_year // 100) + 1
        
        else
            current_century = current_year // 100
        
        if self.century > current_century
            
    
        