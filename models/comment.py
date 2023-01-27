# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Comment(models.Model):
    _name = "sussy_baka.comment"

    # Relations
    post_id = fields.Many2one('sussy_baka.post', string="Post", required=True,
                              help="In which post the comment is")
    student_id = fields.Many2one('res.users', string="Student", required=True,
                                 help="Which user is the creator of the comment")

    # Fields
    comment_text = fields.Text('Comment')
