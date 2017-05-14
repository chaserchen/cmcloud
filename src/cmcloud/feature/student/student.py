# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

import hashlib

import operator
from veil.profile.model import *

db = register_database('cmcloud')


def get_student(id):
    return db().get('SELECT * FROM student WHERE id=%(id)s', id=id)


def check_student_number(number):
    if len(number) != 8:
        raise Invalid('学号格式不正确，需为八位数字')
    return number


@command
def student_sign_in(number=check_student_number, password=not_empty):
    student = db().get('SELECT * FROM student WHERE number=%(number)s', number=number)
    if not student:
        raise InvalidCommand({'mobile': '学号不存在'})
    if student.password != get_student_password(password):
        raise InvalidCommand({'password': '密码错误'})
    return student


@command
def create_student(name=not_empty, number=(not_empty, check_student_number), class_id=to_integer, mobile=(not_empty, is_mobile), email=optional(is_email),
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


@command
def list_students(class_id=to_integer, count=optional(to_integer)):
    count_term = 'ORDER BY RANDOM() LIMIT %(count)s' if count else 'ORDER BY id'
    students = db().list('SELECT * FROM student WHERE class_id=%(class_id)s {}'.format(count_term), class_id=class_id, count=count)
    if count:
        students.sort(key=operator.attrgetter('id'))
    return students


def get_student_password(str):
    return hashlib.md5(str).hexdigest()


def list_student_id2attendance_data(class_id):
    student_id2data = {id: DictObject() for id in list_students(class_id)}
    roll_calls = db().list('''
        SELECT *
        FROM roll_call
        WHERE class_id=%(class_id)s AND created_at>=DATE_TRUNC('month', CURRENT_DATE)
        ''', class_id=class_id)
    for student_id, data in student_id2data.items():
        for roll_call in roll_calls:
            on_count = roll_call.on_student_ids.count(student_id)
            off_count = roll_call.off_student_ids.count(student_id)
            leave_count = roll_call.leave_student_ids.count(student_id)
            if on_count > 0 and off_count > 0 and leave_count > 0:
                data.update(on_count=data.get('on_count', 0) + on_count, off_count=data.get('off_count', 0) + off_count,
                            leave_count=data.get('leave_count', 0) + leave_count)
        total_count = data.on_count + data.off_count + data.leave_count
        data.update(on_rate=round_rate(data.on_count / total_count), off_rate=round_rate(data.off_count / total_count), leave_count=round_rate(total_count))
    return student_id2data


def round_rate(rate):
    return int(rate * 100) / 100
