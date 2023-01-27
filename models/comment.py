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

    @api.onchange('create_date')
    def _check_comment_date_after_post(self):
        comment_date = fields.Datetime.from_string(self.create_date)
        post_date = fields.Datetime.from_String(self.post_id.create_date)
        if comment_date < post_date:
            return {
                'warning' : {
                    'title': 'Warning', 
                    'message': 'Comment creation date can\'t be older than the cration of the post'}
            }    
