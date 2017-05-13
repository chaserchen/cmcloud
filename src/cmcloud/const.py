# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division

from collections import OrderedDict

GENDER_MALE = 1
GENDER_FEMALE = 2
GENDERS = {
    GENDER_MALE: '男',
    GENDER_FEMALE: '女'
}


# three state constants for three-state variables
STATUS_VOID = 0  # 空的，无效的，未开始的
STATUS_INCOMPLETE = 1  # 部分的，不完全的，未完成的，进行中的
STATUS_COMPLETE = 2  # 全部的，完全的，完成的

NOTIFICATION_TYPE_CLASS = 1
NOTIFICATION_TYPE_ACTIVE = 2
NOTIFICATION_TYPE2NAME = OrderedDict((
    (NOTIFICATION_TYPE_CLASS, '课程通知'),
    (NOTIFICATION_TYPE_ACTIVE, '活动通知'),
))

LEAVE_REQUEST_STATUS_PROCESSING = 1
LEAVE_REQUEST_STATUS_ACCEPTED = 2
LEAVE_REQUEST_STATUS_REJECTED = 3
LEAVE_REQUEST_STATUS_REVOKED = 4
LEAVE_REQUEST_STATUS2NAME = {
    LEAVE_REQUEST_STATUS_PROCESSING: '处理中',
    LEAVE_REQUEST_STATUS_ACCEPTED: '请假成功',
    LEAVE_REQUEST_STATUS_REJECTED: '被拒绝',
    LEAVE_REQUEST_STATUS_REVOKED: '已撤销',
}
