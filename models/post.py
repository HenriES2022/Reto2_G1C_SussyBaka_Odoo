# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Post(models.Model):
    _name = "sussy_baka.post"

    # Relations
    comment_ids = fields.One2many('sussy_baka.comment', 'post_id', string='Comments')
    course_id = fields.Many2one('sussy_baka.course', string='Course')

    # Fields
    content_text = fields.Text('Content')
    title = fields.Text('Title')
    img = fields.Binary('Image', help="Insert an image here")
    video = fields.Text('Video')
    
    @api.onchange('create_date')
    def _check_post_date_after_course(self):
        post_date = fields.Datetime.from_string(self.create_date)
        course_date = fields.Datetime.from_string(self.course_id.start_date)
        if post_date < course_date:
            return {
                'warning' : {
                    'title': 'Warning', 
                    'message': 'Post creation date can\'be older than the creation date of the course '}
            }
    
        