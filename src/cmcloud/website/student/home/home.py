# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.web import *

student_route = route_for('student')


@student_route('GET', '/')
def student_home_page():
    redirect_to('/notification')


@widget
def log_out_widget():
    request = get_current_http_request()
    return get_template('log-out-widget.html').render(student=request.student)


@widget
def home_nav_widget():
    return get_template('home-nav-widget.html').render()
