from .position import DimensionHolder
from ..interface import YikObject
from ..dimensions import Dimension


class KinematicsHolder(DimensionHolder): # Already extends YikObject!

    def __init__(self, parent, *args, **kwargs):
        YikObject.__init__(self, parent, *args, **kwargs)
        DimensionHolder.__init__(self, parent, *args, **kwargs)

        self.mass = 1

        self.force = Dimension(0, 0)
        self.acceleration = Dimension(0, 0)
        self.velocity = Dimension(0, 0)

        self.constant_force = Dimension(0, 0)
        self.constant_acceleration = Dimension(0, 0)
        self.constant_velocity = Dimension(0, 0)

    def __pn_kinematics_update_values__(self):
        f = self.constant_force + self.force
        a = self.acceleration + self.constant_acceleration
        v = self.velocity + self.constant_velocity

        a += (f / self.mass)
        v += a

        self.position += v

