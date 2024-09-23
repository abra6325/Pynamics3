import threading
import time

from typing import Union

from .dimensions import Dimension, Dim
from .interface import YikObject
from .logger import Logger
from .timing import sleep, Routine, tps_to_seconds

import traceback
import math

class Renderable(YikObject):

    def __init__(self, parent, screen_position: Union[Dimension, tuple] = Dimension(0, 0), z_index: int = 0):

        self.z_index = z_index

        super().__init__(parent)

        self.screen_position = screen_position




    def __pn_render__(self):

        pass

class RenderNodeSet:

    def __init__(self, z_index=0):
        self.content = set()
        self.z_index = z_index

class RenderQueueIterator:

    def __init__(self):
        pass

    def __next__(self):
        pass



class RenderQueue:

    """
    A modified linked list that allows O(1) insert and O(1) remove.
    """

    def __init__(self):
        self.z_index_dict = {}

    def append(self, object: Renderable):
        """Appends an object to the butt of this queue"""

        if not isinstance(object, Renderable):
            return

        if object.z_index not in self.z_index_dict:
            Logger.debug("Render: New z index created")
            self.z_index_dict[object.z_index] = set()
            self.z_index_dict = {k: v for k, v in sorted(self.z_index_dict.items(), key=lambda item: item[1])}


        self.z_index_dict[object.z_index].add(object)




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

    _yikworks_helper_iconpath = "object_opengl.ico"

    def __init__(self, parent, root, size: Dimension = Dimension(100, 100), scale=1):

        YikObject.__init__(self, parent)
        OpenGLFrame.__init__(self, root, width=size.x, height=size.y)


        self.parent = parent
        self.renderable = RenderQueue()
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

        # Logger.info("Call: draw")

        glClear(GL_COLOR_BUFFER_BIT)
        glFlush()

        for i in self.renderable.z_index_dict:
            for k in self.renderable.z_index_dict[i]:
                k.__pn_render__()

        pass



        #Logger.info("Call: drawend")

    def add_render(self, obj):
        self.renderable.append(obj)


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
            self.gl_canvas.add_render(child)



    def load(self):
        self.root_tk.mainloop()

    def launch(self):
        self._context.launch()
        self.load()










