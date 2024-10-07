

from .simple import RenderableGameObject
from .. import YikObject
from ..logger import Logger
from ..physics.kinematics import KinematicsHolder

try:
    from pyopengltk import OpenGLFrame
    from OpenGL.GL import *
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
except ModuleNotFoundError:
    _import_failure = True
    thing = traceback.format_exc()
    Logger.error(f"Error while importing GL utility: Cannot find GL libraries: \n{thing}")
except ImportError:
    _import_failure = True
    thing = traceback.format_exc()
    Logger.error(f"Error while importing GL utility: Import Error: \n{thing}")

import math

PARTICLE_RESOLUTION = 64


class Particle(RenderableGameObject, KinematicsHolder):



    def __init__(self, parent, *args, **kwargs):
        YikObject.__init__(self, parent, *args, **kwargs)
        RenderableGameObject.__init__(self, parent, primary_initialization=False)
        KinematicsHolder.__init__(self, parent, primary_initialization=False)

    def __pn_routine_update__(self, routine):
        self.__pn_kinematics_update_values__()
        #print("update")

    def __pn_render__(self):

        radius = 10
        glBegin(GL_POLYGON)
        for _ in range(PARTICLE_RESOLUTION):
            cosine = radius * math.cos(_ * 2 * math.pi / PARTICLE_RESOLUTION) + self.x
            sine = radius * math.sin(_ * 2 * math.pi / PARTICLE_RESOLUTION) + self.y
            glVertex2f(cosine, sine)
        glEnd()