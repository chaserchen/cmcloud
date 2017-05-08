from __future__ import unicode_literals, print_function, division
import veil_component

with veil_component.init_component(__name__):
    from .user import remember_current_signed
    from .user import set_current_teacher_on_request
    from .user import set_current_student_on_request

    __all__ = [
        remember_current_signed.__name__,
        set_current_teacher_on_request.__name__,
        set_current_student_on_request.__name__,
    ]
