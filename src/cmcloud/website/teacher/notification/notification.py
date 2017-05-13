# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.web import *

from cmcloud.const import NOTIFICATION_TYPE2NAME
from cmcloud.feature.class_ import *
from cmcloud.feature.notification import *

teacher_route = route_for('teacher')


@teacher_route('GET', '/notification')
def get_notification_page():
    teacher_id = get_current_http_request().teacher_id
    notifications = list_notifications_for_teacher(teacher_id)
    classes = list_classes_by_teacher_id(teacher_id)
    return get_template('notification-page.html').render(notifications=notifications, classes=classes, NOTIFICATION_TYPE2NAME=NOTIFICATION_TYPE2NAME)


@teacher_route('POST', '/notifications')
def create_notification_action():
    create_notification(teacher_id=get_current_http_request().teacher_id, **get_http_arguments())


@teacher_route('DELETE', '/notifications/{{ id }}', id='\d+')
def delete_notification_action():
    delete_notification(get_http_argument('id'), get_current_http_request().teacher_id)
