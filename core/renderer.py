from OpenGL.GL import *

class MyRenderer():
    def __init__(self):
        pass

    def render(self):
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)