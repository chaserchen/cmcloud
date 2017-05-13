# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

import contextlib

from veil.frontend.visitor import *
from veil.frontend.web import *

from cmcloud.feature.student import *
from cmcloud.feature.teacher import *


def remember_current_signed(user_id):
    remember_logged_in_user_id(user_id)


@contextlib.contextmanager
def set_current_teacher_on_request():
    request = get_current_http_request()
    teacher_id = get_logged_in_user_id('teacher')
    teacher = get_teacher(teacher_id)
    request.teacher_id = teacher_id
    request.teacher = teacher
    yield


@contextlib.contextmanager
def set_current_student_on_request():
    request = get_current_http_request()
    student_id = get_logged_in_user_id('student')
    student = get_student(student_id)
    request.student_id = student_id
    request.student = student
    yield
