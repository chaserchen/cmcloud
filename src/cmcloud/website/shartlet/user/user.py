# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

import contextlib

from veil.frontend.visitor import *
from veil.frontend.web import *

from cmcloud.feature.teacher import *


def remember_current_signed(user_id):
    remember_logged_in_user_id(user_id)


@contextlib.contextmanager
def set_current_teacher_on_request():
    request = get_current_http_request()
    teacher_id = get_logged_in_user_id('person')
    teacher = get_teacher(teacher_id)
    request.teacher_id = teacher_id
    request.teacher = teacher
    yield
