from core.window import *
from core.renderer import *

class MyEngine():
    def __init__(self):
        glfwInit()

        glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3)
        glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3)
        glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE)

        try:
            self.window_settings = MyWindowSettings()
            self.window = MyWindow(self.window_settings)
        except RuntimeError as e:
            print(e)

            glfwTerminate()
            raise

        self.renderer = MyRenderer()

    def gameLoop(self):
        while not self.window.shouldClose():
            self.window.pollEvents()
            self.renderer.render()
            self.window.swapBuffers()
    
    def exit(self):
        if self.window:
            self.window.clean()
        
        glfwTerminate()