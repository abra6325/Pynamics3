from .. import YikObject
from ..physics.kinematics import KinematicsHolder
from ..render import Renderable
from ..script import ScriptableObject
from ..timing import CanTick, Routine
from ..physics.position import DimensionHolder

class RenderableGameObject(Renderable, CanTick, ScriptableObject):

    def __init__(self, parent, routine_include=False, *args, **kwargs):
        """

        :param parent: The parent of this object
        :param update: A callable function for this object's routine target. Set to None if this object does not tick.
        """
        YikObject.__init__(self, parent, *args, **kwargs)
        Renderable.__init__(self, parent, primary_initialization=False)
        CanTick.__init__(self, parent, primary_initialization=False, routine_include=routine_include)
        ScriptableObject.__init__(self, parent, primary_initialization=False)

    def __pn_routine_update__(self, routine: Routine = None):
        pass





