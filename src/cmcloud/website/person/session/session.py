# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

from veil.profile.web import *

from cmcloud.feature.teacher import *
from cmcloud.website.shartlet.user import *

person_public_route = route_for('person', tags=(TAG_NO_LOGIN_REQUIRED,))


@person_public_route('GET', '/login')
def login_widget():
    return get_template('login-widget.html').render()


@person_public_route('POST', '/login')
def login_action():
    arguments = get_http_arguments()
    mobile = arguments.mobile
    password = arguments.password
    shopper = teacher_sign_in(mobile, password)
    remember_current_signed(shopper.id)
    return arguments.get('ru', '/')


@person_public_route('GET', '/logout')
def logout_action():
    remove_logged_in_user_id('person')
    redirect_to('/login')
