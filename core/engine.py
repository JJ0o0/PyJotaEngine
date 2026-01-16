from core.window import *
from core.renderer import *

class MyEngine():
    """
    Main engine class responsible for managing the window, renderer, and game loop.

    This class initializes GLFW, creates the window and OpenGL context, sets up the 
    renderer, and runs the main game loop until the window is closed.

    ...

    Attributes
    ----------
    window_settings : MyWindowSettings
        the current window settings.
    window : MyWindow
        the current window object.
    renderer : MyRenderer
        the current engine renderer.
    
    Methods
    ----------
    gameLoop()
        Runs the main loop, processing events and rendering each frame.
    exit()
        Cleans up and terminates all engine resources.
    """
    
    def __init__(self):
        """
        Initialize GLFW, create window and renderer.

        Raises
        ------
        RuntimeError
            If the window could not be created.
        """

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
        """
        Runs every frame until the end of the window object's life.
        """

        while not self.window.shouldClose():
            self.window.pollEvents()
            self.renderer.render()
            self.window.swapBuffers()
    
    def exit(self):
        """
        Cleans the engine's leftovers.
        """
        
        if self.window:
            self.window.clean()
        
        glfwTerminate()