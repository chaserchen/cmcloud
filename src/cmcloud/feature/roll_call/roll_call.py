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
