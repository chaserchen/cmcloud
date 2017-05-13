# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.web import *

from cmcloud.const import NOTIFICATION_TYPE2NAME, LEAVE_REQUEST_STATUS2NAME


@template_filter('notification_type')
def render_notification_type(type):
    return NOTIFICATION_TYPE2NAME[type]


@template_filter('leave_request_status')
def render_leave_request_status(status):
    return LEAVE_REQUEST_STATUS2NAME[status]
