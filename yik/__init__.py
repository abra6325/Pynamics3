


from .interface import YikObject, NullObject, NameGenerator
from .application import ApplicationObject

NameGenerator.__init__()

def set_naming_seed(seed: int) -> None:
    """
    Sets the seed for the random name generator when a name is unspecified. It is recommended to set a name
    so that it ensures references are identical every run.
    :param seed: The seed to set.
    :return: None
    """
    NameGenerator.set_seed(seed)

from .render import WindowGLFW, WindowGLTk

from .yikworks.ui import YikWorksUI

from .event_arguments import EventArgument
from .events_enum import  EVENTS

from .context import World
from .timing import Timer
from .gameobject.simple import RenderableGameObject
from .gameobject.particle import Particle
from .events_reworked import EventBus
from .event_arguments import *





