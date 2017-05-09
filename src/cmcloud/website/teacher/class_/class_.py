# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from veil.profile.web import *

from cmcloud.feature.class_ import *

teacher_route = route_for('teacher')


@teacher_route('GET', '/class-management')
def get_class_management_page():
    return get_template('class-management.html').render()


@teacher_route('GET', '/classes')
@widget
def list_classes_widget():
    return get_template('list-classes-widget.html').render(classes=list_classes())


@teacher_route('POST', '/classes')
def create_class_action():
    create_class(**get_http_arguments())
