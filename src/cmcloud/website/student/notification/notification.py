# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.web import *

from cmcloud.feature.notification import *

student_route = route_for('student')


@student_route('GET', '/notification')
def get_notification_page():
    notifications = list_notifications_for_student(get_current_http_request().student_id)
    return get_template('notification-page.html').render(notifications=notifications)
