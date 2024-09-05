import threading
import time

from .dimensions import Dimension, Dim
from .interface import YikObject
from .logger import Logger
from .timing import sleep, Routine, tps_to_seconds

import traceback


class WindowGLFW(YikObject):

    def __post_init__(self):

            # Set OpenGL version (optional, depending on your needs)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        # Create a windowed mode window and its OpenGL context
        window = glfw.create_window(500, 500, "Simple Canvas", None, None)
        if not window:
            glfw.terminate()
            return None

        # Make the window's context current
        glfw.make_context_current(window)

_import_failure = False

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

class DummyOpenGLFrame:

    def __init__(self, *args, **kwargs):
        Logger.warn("Using DummyOpenGLFrame")

    def pack(self, *args, **kwargs):
        Logger.warn("DummyOpenGLFrame.pack: Using DummyOpenGLFrame")

if _import_failure:
    OpenGLFrame = DummyOpenGLFrame


class WindowGLTkCanvas(OpenGLFrame, YikObject):

    def __init__(self, parent, root, size: Dimension = Dimension(100, 100), scale=1):
        OpenGLFrame.__init__(self, root, width=size.x, height=size.y)
        YikObject.__init__(self, parent)
        self.parent = parent
        self.renderable = []
        self.scale = scale

        self.texture_handler = {}

        self.width = size.x
        self.height = size.y




    def initgl(self):
        Logger.info("Call: initgl")
        glViewport(0, 0, self.width, self.height)
        glClearColor(0, 0, 0, 0)

        # setup projection matrix
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self.width, self.height, 0, -1, 1)

        # setup identity model view matrix
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glEnable(GL_TEXTURE_2D)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        #glEnable(GL_LINE_SMOOTH)

    def redraw(self):

        #Logger.info("Call: draw")

        glClear(GL_COLOR_BUFFER_BIT)
        glFlush()

        #Logger.info("Call: drawend")


import tkinter as tk

class WindowGLTk(YikObject):

    def __init__(self, parent, name=None):
        super().__init__(parent, name=name)

        self.root_tk = tk.Tk()
        self.gl_canvas = WindowGLTkCanvas(self, self.root_tk, Dim(500, 500))
        self.gl_canvas.pack(fill=tk.BOTH, expand=tk.YES)
        self.gl_canvas.animate = True

        self._context = None

        #self.frame = Routine(self, self._tick, delay=tps_to_seconds(200))

    def __leaf_added__(self, child):
        if isinstance(child, Renderable):
            Logger.debug(f"{self} notices {child} as Renderable.")

    def load(self):
        self.root_tk.mainloop()

    def launch(self):
        self._context.launch()
        self.load()




class Renderable(YikObject):

    def __init__(self, parent, screen_position=Dimension(0, 0)):
        super().__init__(parent)

        self.screen_position = screen_position

    def __pn_render__(self):
        pass





