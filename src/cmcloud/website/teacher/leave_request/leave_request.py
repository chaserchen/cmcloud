# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.web import *

from cmcloud.feature.leave_request import *

teacher_route = route_for('teacher')


@teacher_route('GET', '/leave-request')
def get_leave_request_page():
    return get_template('leave-request.html').render(leave_requests=list_processing_leave_requests_for_teacher(get_current_http_request().teacher_id))


@teacher_route('PUT', '/leave-requests/{{ id }}/accept', id='\d+')
def accept_leave_request_action():
    accept_leave_request(teacher_id=get_current_http_request().teacher_id, **get_http_arguments())


@teacher_route('PUT', '/leave-requests/{{ id }}/reject', id='\d+')
def reject_leave_request_action():
    reject_leave_request(teacher_id=get_current_http_request().teacher_id, **get_http_arguments())
