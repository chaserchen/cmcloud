# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

from veil.profile.web import *

from cmcloud.feature.teacher import *
from cmcloud.website.shartlet.user import *

teacher_public_route = route_for('teacher', tags=(TAG_NO_LOGIN_REQUIRED,))


@teacher_public_route('GET', '/login')
def login_widget():
    return get_template('login-widget.html').render()


@teacher_public_route('POST', '/login')
def login_action():
    shopper = teacher_sign_in(get_http_argument('mobile'), get_http_argument('password'))
    remember_current_signed(shopper.id)
    return get_http_argument('ru', default='/')


@teacher_public_route('GET', '/logout')
def logout_action():
    remove_logged_in_user_id('teacher')
    redirect_to('/login')
