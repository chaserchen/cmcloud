# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.model import *

db = register_database('cmcloud')


@command
def list_homeworks_by_teacher_id(teacher_id=to_integer):
    return db().list('''
        SELECT h.*, c.name AS class_name
        FROM homework h
            INNER JOIN class c ON c.id=h.class_id
        WHERE h.teacher_id=%(teacher_id)s AND created_at>=(CURRENT_TIMESTAMP - INTERVAL '1 MONTHS')
        ''', teacher_id=teacher_id)


@command
def create_homework(teacher_id=to_integer, class_id=to_integer, content=clamp_length(min=1, max=250)):
    db().insert('homework', teacher_id=teacher_id, class_id=class_id, content=content)
