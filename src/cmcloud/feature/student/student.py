# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

import hashlib

from veil.profile.model import *

db = register_database('cmcloud')


def get_student(id):
    return db().get('SELECT * FROM student WHERE id=%(id)s', id=id)


@command
def student_sign_in(mobile=(not_empty, is_mobile), password=not_empty):
    student = db().get('SELECT * FROM student WHERE mobile=%(mobile)s', mobile=mobile)
    if not student:
        raise InvalidCommand({'mobile': '未注册'})
    if student.password != get_student_password(password):
        raise InvalidCommand({'password': '密码错误'})
    return student


def check_student_code(number):
    if len(number) != 8:
        raise Invalid('学号格式不正确，需为八位数字')
    return number


@command
def create_student(name=not_empty, number=(not_empty, check_student_code), class_id=to_integer, mobile=(not_empty, is_mobile), email=optional(is_email),
                   password=not_empty, password_confirm=not_empty):
    if not db().exists('SELECT 1 FROM class WHERE id=%(class_id)s', class_id=class_id):
        raise InvalidCommand({'class_id': '班级不存在'})
    if password != password_confirm:
        raise InvalidCommand({'password_confirm': '两次输入的密码不一致'})
    student_id = db().insert('student', returns_id=True, conflict_target='(number)', conflict_action='DO NOTHING', name=name, number=number, class_id=class_id,
                             mobile=mobile, email=email, password=get_student_password(password))
    if not student_id:
        raise InvalidCommand({'number': '该学号已被注册'})
    return student_id


def get_student_password(str):
    return hashlib.md5(str).hexdigest()

