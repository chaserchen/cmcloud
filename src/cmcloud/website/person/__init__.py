from __future__ import unicode_literals, print_function, division
import veil_component
from veil.frontend.visitor import enable_user_tracking


with veil_component.init_component(__name__):
    __all__ = []

    def init():
        from veil.frontend.web import register_website_context_manager
        from veil.frontend.visitor import enable_visitor_origin_tracking
        from cmcloud.website.shartlet.user import set_current_teacher_on_request

        register_website_context_manager('person', enable_visitor_origin_tracking())
        register_website_context_manager('person', enable_user_tracking('person', login_url='/login'))
        register_website_context_manager('person', set_current_teacher_on_request)
