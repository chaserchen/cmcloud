# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.model import *
import hashlib

db = register_database('cmcloud')


@command
def teacher_sign_in(mobile=is_mobile, password=not_empty):
    teacher = db().get('SELECT * FROM teacher WHERE mobile=%(mobile)s', mobile=mobile)
    if not teacher:
        raise InvalidCommand({'mobile': '未添加该教师'})
    if teacher.password != get_teacher_password(password):
        raise InvalidCommand({'password': '密码错误'})
    return teacher


def get_teacher(id):
    return db().get('SELECT * FROM teacher WHERE id=%(id)s', id=id)


@command
def create_teacher(name=not_empty, mobile=is_mobile, email=optional(is_email), is_super=optional(to_bool, default=False)):
    teacher_id = db().insert('teacher', returns_id=True, conflict_target='(mobile)', conflict_action='DO NOTHING', name=name, mobile=mobile, email=email,
                             password=get_teacher_password(mobile), is_super=is_super)
    if not teacher_id:
        raise InvalidCommand({'mobile': '该手机号已创建教师账号'})


def get_teacher_password(str):
    return hashlib.md5(str).hexdigest()
