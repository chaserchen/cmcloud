# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.model import *

db = register_database('cmcloud')


@command
def create_roll_call(class_id=to_integer, on_student_ids=is_list, off_student_ids=is_list, leave_student_ids=is_list):
    on_student_ids, off_student_ids, leave_student_ids = set(on_student_ids), set(off_student_ids), set(leave_student_ids)
    if on_student_ids & off_student_ids or on_student_ids & leave_student_ids or off_student_ids & leave_student_ids:
        raise InvalidCommand({'@': '数据错误，请重新点名并提交'})
    db().insert('roll_call', class_id=class_id, on_student_ids=list(on_student_ids), off_student_ids=list(off_student_ids),
                leave_student_ids=list(leave_student_ids))


@command
def get_latest_roll_call(class_id=to_integer):
    return db().get('SELECT * FROM roll_call WHERE class_id=%(class_id)s ORDER BY ID DESC LIMIT 1', class_id=class_id)


@command
def list_roll_call(class_id=to_integer):
    return db().list('''
        SELECT rc.id, rc.class_id, rc.created_at,
            ARRAY(SELECT ROW_TO_JSON(s1.*) FROM student s1 WHERE s1.id=ANY(rc.on_student_ids)) AS on_students,
            ARRAY(SELECT ROW_TO_JSON(s2.*) FROM student s2 WHERE s2.id=ANY(rc.off_student_ids)) AS off_students,
            ARRAY(SELECT ROW_TO_JSON(s3.*) FROM student s3 WHERE s3.id=ANY(rc.leave_student_ids)) AS leave_students
        FROM roll_call rc
        WHERE class_id=%(class_id)s
        GROUP BY rc.id
        ORDER BY id DESC
        ''', class_id=class_id)
