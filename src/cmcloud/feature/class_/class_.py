# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.model import *

db = register_database('cmcloud')


def list_classes():
    return db().list('SELECT * FROM class ORDER BY id')


@command
def list_classes_by_teacher_id(teacher_id=to_integer):
    return db().list('''
        SELECT c.*
        FROM class c
            INNER JOIN teacher t ON c.id=ANY(t.class_ids)
        WHERE t.id=%(teacher_id)s
        ''', teacher_id=teacher_id)


def check_class_code(code):
    if len(code) != 6:
        raise Invalid('班级代码不正确，需为六位数字')
    return code


@command
def create_class(code=(not_empty, check_class_code), name=not_empty):
    class_id = db().insert('class', returns_id=True, conflict_target='(code)', conflict_action='DO NOTHING', code=code, name=name)
    if not class_id:
        raise InvalidCommand({'number': '该班级代码已被使用'})
