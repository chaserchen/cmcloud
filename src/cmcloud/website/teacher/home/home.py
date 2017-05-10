# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.web import *

teacher_route = route_for('teacher')


@teacher_route('GET', '/')
def teacher_home_page():
    return get_template('home-page.html').render()


@widget
def log_out_widget():
    request = get_current_http_request()
    return get_template('log-out-widget.html').render(teacher=request.teacher)


@widget
def home_nav_widget():
    return get_template('home-nav-widget.html').render()
