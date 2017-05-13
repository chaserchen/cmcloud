# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.web import *

from cmcloud.feature.class_ import *
from cmcloud.feature.homework import *

teacher_route = route_for('teacher')


@teacher_route('GET', '/homework')
def get_homework_page():
    teacher_id = get_current_http_request().teacher_id
    classes = list_classes_by_teacher_id(teacher_id)
    return get_template('homework-page.html').render(classes=classes, homeworks=list_homeworks_by_teacher_id(teacher_id))


@teacher_route('POST', '/homeworks')
def create_homework_action():
    create_homework(teacher_id=get_current_http_request().teacher_id, **get_http_arguments())
