# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.web import *
from cmcloud.feature.person import *

person_route = route_for('person')


@person_route('GET', '/')
def teacher_home_page():
    request = get_current_http_request()
    print(request.teacher)
    return get_template('home-page.html').render(persons=list_persons())


@widget
def log_out_widget():
    request = get_current_http_request()
    return get_template('log-out-widget.html').render(teacher=request.teacher)
