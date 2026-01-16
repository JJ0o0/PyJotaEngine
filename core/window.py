from glfw.GLFW import *
from OpenGL.GL import glViewport
from settings.window_settings import MyWindowSettings

class MyWindow():
    def __init__(self, settings : MyWindowSettings):
        self.settings = settings
        self.window = glfwCreateWindow(self.settings.width, self.settings.height, self.settings.title, None, None)

        if not self.window:
            raise RuntimeError("ERRO: Não foi possível criar a janela.")

        glfwMakeContextCurrent(self.window)
        glfwSetFramebufferSizeCallback(self.window, self.framebufferSizeCallback)


    def pollEvents(self):
        glfwPollEvents()
    
    def swapBuffers(self):
        glfwSwapBuffers(self.window)
    
    def shouldClose(self):
        return glfwWindowShouldClose(self.window)

    def clean(self):
        glfwDestroyWindow(self.window)
    
    @staticmethod
    def framebufferSizeCallback(window, width, height):
        glViewport(0, 0, width, height)