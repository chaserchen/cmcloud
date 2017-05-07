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
    if teacher.password != hashlib.md5(password).hexdigest():
        raise InvalidCommand({'password': '密码错误'})
    return teacher


def get_teacher(id):
    return db().get('SELECT * FROM teacher WHERE id=%(id)s', id=id)
