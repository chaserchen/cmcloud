# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

from veil.profile.web import *

from cmcloud.feature.class_ import *
from cmcloud.feature.student import *
from cmcloud.website.shartlet.user import *

student_public_route = route_for('student', tags=(TAG_NO_LOGIN_REQUIRED,))


@student_public_route('GET', '/login')
def login_widget():
    return get_template('login-widget.html').render()


@student_public_route('POST', '/login')
def login_action():
    shopper = student_sign_in(**get_http_arguments())
    remember_current_signed(shopper.id)
    return get_http_argument('ru', default='/')


@student_public_route('GET', '/logout')
def logout_action():
    remove_logged_in_user_id('student')
    redirect_to('/login')


@student_public_route('GET', '/register')
def register_widget():
    return get_template('register-widget.html').render(classes=list_classes())


@student_public_route('POST', '/register')
def register_action():
    student_id = create_student(**get_http_arguments())
    remember_current_signed(student_id)
    return get_http_argument('ru', default='/')
