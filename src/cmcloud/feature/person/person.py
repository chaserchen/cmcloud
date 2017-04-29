# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
import logging
from veil.profile.web import *
from veil.profile.model import *
from cmcloud.const import GENDERS

LOGGER = logging.getLogger(__name__)
db = register_database('cmcloud')


def list_persons():
    return db().list('SELECT * FROM person ORDER BY id')


@template_filter('gender')
def render_gender(value):
    return GENDERS[value]
