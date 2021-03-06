# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.model import *
import hashlib

db = register_database('cmcloud')


def check_teacher_number(number):
    if len(number) != 8:
        raise Invalid('工号格式不正确，需为八位数字')
    return number


@command
def teacher_sign_in(number=check_teacher_number, password=not_empty):
    teacher = db().get('SELECT * FROM teacher WHERE number=%(number)s', number=number)
    if not teacher:
        raise InvalidCommand({'number': '工号不存在'})
    if teacher.password != get_teacher_password(password):
        raise InvalidCommand({'password': '密码错误'})
    return teacher


def get_teacher(id):
    return db().get('SELECT * FROM teacher WHERE id=%(id)s', id=id)


@command
def create_teacher(name=not_empty, number=(not_empty, check_teacher_number), mobile=(not_empty, is_mobile), email=optional(is_email),
                   is_super=optional(to_bool, default=False)):
    teacher_id = db().insert('teacher', returns_id=True, conflict_target='(number)', conflict_action='DO NOTHING', name=name, number=number, mobile=mobile,
                             email=email, password=get_teacher_password(mobile), is_super=is_super)
    if not teacher_id:
        raise InvalidCommand({'number': '该工号已被注册'})
    return teacher_id


def get_teacher_password(str):
    return hashlib.md5(str).hexdigest()
