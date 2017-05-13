# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.model import *

from cmcloud.const import NOTIFICATION_TYPE2NAME

db = register_database('cmcloud')


@command
def list_notifications_for_teacher(teacher_id=to_integer):
    return db().list('''
        SELECT n.*, c.name AS class_name
        FROM notification n
            LEFT JOIN class c ON c.id=n.class_id
        WHERE n.teacher_id=%(teacher_id)s AND created_at>=(CURRENT_TIMESTAMP - INTERVAL '3 MONTHS')
        ORDER BY n.id DESC
        ''', teacher_id=teacher_id)


@command
def list_notifications_for_student(student_id=to_integer):
    return db().list('''
        SELECT *
        FROM notification n
        WHERE class_id IS NULL OR class_id=(SELECT class_id FROM student WHERE id=%(student_id)s)
        ORDER BY id DESC
        ''', student_id=student_id)


@command
def create_notification(teacher_id=to_integer, class_id=optional(to_integer), type=(to_integer, one_of(NOTIFICATION_TYPE2NAME)),
                        content=clamp_length(min=1, max=250)):
    db().insert('notification', teacher_id=teacher_id, class_id=class_id, type=type, content=content)


@command
def delete_notification(id=to_integer, teacher_id=to_integer):
    db().execute('DELETE FROM notification WHERE id=%(id)s AND teacher_id=%(teacher_id)s', id=id, teacher_id=teacher_id)
