# -*- coding: utf-8 -*-
{
    'name': "Sussy Baka - Online Course Manager",

    'summary': 'This module manages a online course',

    'description': """
        This module manages a online course, with the following data:
        - Courses
        - Subjects that a teacher is specialized
        - Relation between student and courses
        - Relation between teacher and courses
        - Posts and comments in them
        
    """,

    'author': "Sussy Baka S.A.",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','report'],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'report/report.xml',
        'report/post_report.xml',
        'views/views.xml',
        'views/course_view.xml',
        'views/post_view.xml',
        'views/subject_view.xml',
        'views/templates.xml',
        'views/user_view.xml',
    ],
    'installable': True, 
    'auto_install': False

}
