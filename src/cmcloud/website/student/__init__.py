from __future__ import unicode_literals, print_function, division
import veil_component
from veil.frontend.visitor import enable_user_tracking
from cmcloud.website.sharelet import template_helpers
template_helpers.render_notification_type(1)

with veil_component.init_component(__name__):
    __all__ = []

    def init():
        from veil.frontend.web import register_website_context_manager
        from veil.frontend.visitor import enable_visitor_origin_tracking
        from cmcloud.website.sharelet.user import set_current_student_on_request

        register_website_context_manager('student', enable_visitor_origin_tracking())
        register_website_context_manager('student', enable_user_tracking('student', login_url='/login'))
        register_website_context_manager('student', set_current_student_on_request)
