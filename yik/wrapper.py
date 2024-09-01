from .render import WindowGLTk
from .interface import NullObject
from .context import World


def create_standard_context() -> WindowGLTk:
    """
    Constructs a WindowGLTk with context World and a routine.
    :return: WindowGLTk
    """

    a = WindowGLTk(NullObject())
    b = World(a)