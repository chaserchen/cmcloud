# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

from pprint import pprint

from veil.profile.web import *

from cmcloud.feature.class_ import *
from cmcloud.feature.roll_call import *

teacher_route = route_for('teacher')


@teacher_route('GET', '/')
def teacher_home_page():
    classes = list_classes_by_teacher_id(get_current_http_request().teacher_id)
    return get_template('home-page.html').render(classes=classes)


@teacher_route('GET', '/class-home')
@widget
def class_home_widget(class_id=None):
    class_id = class_id or get_http_argument('claeess_id', optional=True)
    roll_call = get_latest_roll_call(class_id)
    return get_template('class-home-widget.html').render(class_id=class_id, roll_call=roll_call)


@teacher_route('GET', '/classes/{{ class_id }}/roll-call-list', class_id='\d+')
def list_roll_call_page():
    class_id = get_http_argument('class_id')
    roll_call_list = list_roll_call(class_id)
    pprint(roll_call_list)
    return get_template('roll-call-list.html').render(roll_call_list=roll_call_list)


@widget
def log_out_widget():
    request = get_current_http_request()
    return get_template('log-out-widget.html').render(teacher=request.teacher)


@widget
def home_nav_widget():
    return get_template('home-nav-widget.html').render()
