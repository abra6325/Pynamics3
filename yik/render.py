import threading
import time

from glfw.library import glfw

from pynamics.dimensions import Dimension, Dim
from pynamics.interface import PynamicsObject
from pynamics.logger import Logger
from pynamics.timing import sleep, Routine, tps_to_seconds


class WindowGLFW(PynamicsObject):

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

from pyopengltk import OpenGLFrame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



class WindowGLTkCanvas(OpenGLFrame, PynamicsObject):

    def __init__(self, parent, root, size: Dimension = Dimension(100, 100), scale=1):

        OpenGLFrame.__init__(self, root, width=size.x, height=size.y)
        PynamicsObject.__init__(self, parent)
        self.parent = parent
        self.renderable = []
        self.scale = scale

        self.texture_handler = {}

        self.width = size.x
        self.height = size.y

        self.frame = Routine(self, target=self.redraw)


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

class WindowGLTk(PynamicsObject):

    def __init__(self, parent):
        super().__init__(parent)

        self.root = tk.Tk()
        self.gl_canvas = WindowGLTkCanvas(self, self.root, Dim(500, 500))
        self.gl_canvas.pack(fill=tk.BOTH, expand=tk.YES)
        self.gl_canvas.animate = True

        self.parent._viewport = self

        #self.frame = Routine(self, self._tick, delay=tps_to_seconds(200))

    def load(self):
        self.root.mainloop()



