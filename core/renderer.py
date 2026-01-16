from OpenGL.GL import *

# TODO: Docstring for the renderer class.
class MyRenderer():
    def __init__(self):
        pass

    # TODO: Proper rendering.
    def render(self):
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)