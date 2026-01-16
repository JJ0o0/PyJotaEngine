class MyWindowSettings():
    """
    A class used as a container for the Game Window Settings

    ...

    Attributes
    ----------
    width : int
        the window width (default is 800)
    height : int
        the window height (default is 600)
    title : str
        the window title (default is "PyJotaEngine")
    """

    def __init__(self, width = 800, height = 600, title = "PyJotaEngine"):
        """
        Parameters
        ----------
        width : int, optional
            the window width (default is 800)
        height : int, optional
            the window height (default is 600)
        title : str, optional
            the window title (default is "PyJotaEngine")
        """

        self.width = width
        self.height = height
        self.title = title