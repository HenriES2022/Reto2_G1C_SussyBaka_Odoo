# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Post(models.Model):
    _name = "sussy_baka.post"

    # Relations
    comment_ids = fields.One2many(
        'sussy_baka.comment', 'post_id', string='Comments')
    course_id = fields.Many2one('sussy_baka.course', string='Course')

    # Fields
    content_text = fields.Text('Content')
    img = fields.Binary('Image', help="Insert an image here")
    #video = 
    