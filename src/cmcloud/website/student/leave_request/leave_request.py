# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.web import *

from cmcloud.feature.leave_request import *

student_route = route_for('student')


@student_route('GET', '/leave-request')
def get_leave_request_page():
    return get_template('leave-request.html').render(leave_requests=list_leave_requests_for_student(get_current_http_request().student_id))


@student_route('POST', '/leave-requests')
def create_leave_request_action():
    create_leave_request(student_id=get_current_http_request().student_id, reason=get_http_argument('reason'))


@student_route('PUT', '/leave-requests/{{ id }}/revoke', id='\d+')
def revoke_leave_request_action():
    revoke_leave_request(get_http_argument('id'), get_current_http_request().student_id)
