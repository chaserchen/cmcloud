# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.model import *

from cmcloud.const import LEAVE_REQUEST_STATUS_PROCESSING, LEAVE_REQUEST_STATUS_ACCEPTED, LEAVE_REQUEST_STATUS_REJECTED, LEAVE_REQUEST_STATUS_REVOKED

db = register_database('cmcloud')


@command
def create_leave_request(student_id=to_integer, reason=clamp_length(min=1, max=250)):
    db().insert('leave_request', student_id=student_id, reason=reason)


@command
def list_leave_requests_for_student(student_id=to_integer):
    leave_requests = db().list('''
        SELECT lr.*, t.name AS teacher_name
        FROM leave_request lr
            LEFT JOIN teacher t ON t.id=lr.teacher_id
        WHERE lr.student_id=%(student_id)s AND lr.created_at>=(CURRENT_TIMESTAMP - INTERVAL '1 MONTHS')
        ORDER BY id DESC
        ''', student_id=student_id)
    attach_leave_requests_with_additional_data(leave_requests)
    return leave_requests


@command
def list_processing_leave_requests_for_teacher(teacher_id=to_integer):
    leave_requests = db().list('''
        SELECT lr.*
        FROM leave_request lr
            INNER JOIN student s ON s.id=lr.student_id
        WHERE lr.status=%(LEAVE_REQUEST_STATUS_PROCESSING)s
            AND lr.created_at>=(CURRENT_TIMESTAMP - INTERVAL '1 MONTHS')
        ORDER BY id
        ''', teacher_id=teacher_id, LEAVE_REQUEST_STATUS_PROCESSING=LEAVE_REQUEST_STATUS_PROCESSING)
    attach_leave_requests_with_additional_data(leave_requests)
    return leave_requests


@command
def revoke_leave_request(id=to_integer, student_id=to_integer):
    db().execute('''
        UPDATE leave_request
        SET status=%(LEAVE_REQUEST_STATUS_REVOKED)s, processed_at=CURRENT_TIMESTAMP
        WHERE id=%(id)s AND student_id=%(student_id)s AND status=%(LEAVE_REQUEST_STATUS_PROCESSING)s
        ''', id=id, student_id=student_id, LEAVE_REQUEST_STATUS_PROCESSING=LEAVE_REQUEST_STATUS_PROCESSING,
                 LEAVE_REQUEST_STATUS_REVOKED=LEAVE_REQUEST_STATUS_REVOKED)


@command
def accept_leave_request(id=to_integer, teacher_memo=optional(clamp_length(min=1, max=250)), teacher_id=to_integer):
    db().execute('''
        UPDATE leave_request
        SET status=%(LEAVE_REQUEST_STATUS_ACCEPTED)s, teacher_id=%(teacher_id)s, teacher_memo=%(teacher_memo)s, processed_at=CURRENT_TIMESTAMP
        WHERE id=%(id)s AND status=%(LEAVE_REQUEST_STATUS_PROCESSING)s
        ''', id=id, teacher_id=teacher_id, teacher_memo=teacher_memo, LEAVE_REQUEST_STATUS_PROCESSING=LEAVE_REQUEST_STATUS_PROCESSING,
                 LEAVE_REQUEST_STATUS_ACCEPTED=LEAVE_REQUEST_STATUS_ACCEPTED)


@command
def reject_leave_request(id=to_integer, teacher_memo=optional(clamp_length(min=1, max=250)), teacher_id=to_integer):
    db().execute('''
        UPDATE leave_request
        SET status=%(LEAVE_REQUEST_STATUS_REJECTED)s, teacher_id=%(teacher_id)s, teacher_memo=%(teacher_memo)s, processed_at=CURRENT_TIMESTAMP
        WHERE id=%(id)s AND status=%(LEAVE_REQUEST_STATUS_PROCESSING)s
        ''', id=id, teacher_id=teacher_id, teacher_memo=teacher_memo, LEAVE_REQUEST_STATUS_PROCESSING=LEAVE_REQUEST_STATUS_PROCESSING,
                 LEAVE_REQUEST_STATUS_REJECTED=LEAVE_REQUEST_STATUS_REJECTED)


def attach_leave_requests_with_additional_data(leave_requests):
    for request in leave_requests:
        request.is_processing = request.status == LEAVE_REQUEST_STATUS_PROCESSING
        request.is_accepted = request.status == LEAVE_REQUEST_STATUS_ACCEPTED
        request.is_rejected = request.status == LEAVE_REQUEST_STATUS_REJECTED
        request.is_revoked = request.status == LEAVE_REQUEST_STATUS_REVOKED
