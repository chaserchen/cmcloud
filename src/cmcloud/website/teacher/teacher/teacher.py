# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.web import *

from cmcloud.feature.teacher import *

teacher_route = route_for('teacher')


@teacher_route('GET', '/teachers/new')
def get_teacher_new_page():
    current_teacher = get_current_http_request().teacher
    if not current_teacher.is_super:
        set_http_status_code(httplib.FORBIDDEN)
        return
    return get_template('teacher-new.html').render()


@teacher_route('POST', '/teachers')
def create_teacher_action():
    create_teacher(**get_http_arguments())
