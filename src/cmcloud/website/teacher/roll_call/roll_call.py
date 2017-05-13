# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

from veil.profile.web import *

from cmcloud.feature.class_ import *
from cmcloud.feature.roll_call import *
from cmcloud.feature.student import *

teacher_route = route_for('teacher')


@teacher_route('GET', '/roll-call')
def get_roll_call_page():
    teacher_id = get_current_http_request().teacher_id
    classes = list_classes_by_teacher_id(teacher_id)
    return get_template('roll-call.html').render(classes=classes)


@teacher_route('GET', '/classes/{{ class_id }}/roll-call', class_id='\d+')
@widget
def roll_call_with_class_widget(class_id=None):
    class_id = class_id or get_http_argument('class_id')
    is_partial = get_http_argument('is_partial', to_type=to_bool, default=False)
    count = get_http_argument('count', to_type=int, optional=True)
    return get_template('create-roll-call.html').render(class_id=class_id, students=list_students(class_id, count), is_partial=is_partial)


@teacher_route('POST', '/classes/{{ class_id }}/roll-call', class_id='\d+')
def roll_call_with_class_action():
    create_roll_call(**get_http_arguments())

