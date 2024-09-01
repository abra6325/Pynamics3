from .gameobject.simple import GameObject
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

def create_game_object(isolate_thread=False, thread_frequency=128):
    """

    :param isolate_thread: If this is true, then this game object will have its own ticking thread
    :param thread_frequency: The frequency of this game object's isolated thread.
    :return:
    """

    a = GameObject()
    return a