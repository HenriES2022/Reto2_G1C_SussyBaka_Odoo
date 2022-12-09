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
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}