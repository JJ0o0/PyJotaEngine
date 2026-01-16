from glfw.GLFW import *
from OpenGL.GL import glViewport
from settings.window_settings import MyWindowSettings

class MyWindow():
    """
    A class used to represent the Game Window

    ...

    Attributes
    ----------
    settings : MyWindowSettings
        the current window settings
    window : Any
        the current glfw window object
    
    Methods
    ----------
    pollEvents()
        Call glfwPollEvents() from glfw library
    swapBuffers()
        Call glfwSwapBuffers() using the current glfw window object as a parameter
    shouldClose()
        Returns if the current glfw window should close, using glfwWindowShouldClose() 
        and the current glfw window object as the function parameter
    clean()
        Destroys the window object using glfw
    framebufferSizeCallback(window : Any, width : int, height : int)
        Static callback function that invokes when the framebuffer is resized
    """

    def __init__(self, settings : MyWindowSettings):
        """
        Parameters
        ----------
        settings : MyWindowSettings
            Current window settings
        
        Raises
        ----------
        RuntimeError
            If the window couldn't be created
        """

        self.settings = settings
        self.window = glfwCreateWindow(self.settings.width, self.settings.height, self.settings.title, None, None)

        if not self.window:
            raise RuntimeError("ERRO: Não foi possível criar a janela.")

        glfwMakeContextCurrent(self.window)
        glfwSetFramebufferSizeCallback(self.window, self.framebufferSizeCallback)

    def pollEvents(self):
        """
        Calls glfwPollEvents() from GLFW library.

        This function should be called once per frame before the start of 
        any other process on the game loop.
        """

        glfwPollEvents()
    
    def swapBuffers(self):
        """
        Calls glfwSwapBuffers() using current window object as parameter.

        This function should be called once per frame after all 
        rendering and processing for the current frame is done.
        """

        glfwSwapBuffers(self.window)
    
    def shouldClose(self) -> bool:
        """
        Get if the current window should close using glfw library.

        Returns
        ----------
        bool
            the current state of glfwWindowShouldClose() using the current window object as 
            parameter
        """

        return glfwWindowShouldClose(self.window)

    def clean(self):
        """
        Destroys the current GLFW window object and releases associated resources.
        """

        glfwDestroyWindow(self.window)
    
    @staticmethod
    def framebufferSizeCallback(window, width, height):
        """
        Change current viewport size based on the current window size.

        Parameters
        ----------
        window : Any
            the current window object
        width : int
            the current window width
        height : int
            the current window height

        Notes
        ----------
        This function is registered with glfwSetFramebufferSizeCallback and should not be
        called directly.
        """

        glViewport(0, 0, width, height)