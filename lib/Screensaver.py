import tkinter

class Screensaver:
    def __init__(self, inactivityDuration: int = 1000):
        self.inactivityDuration = inactivityDuration
        self.window = tkinter.Tk()
        self.timer = None
        self._initializeWindow()
    
    def run(self):
        """Starts the screensaver application."""
        self._startInactivityTimer()
        self.window.mainloop()

    def exit(self, event: tkinter.Event = None):
        """Exits the screensaver."""
        self._stopTimer()
        self.window.destroy()
    
    def _initializeWindow(self):
        """Initializes the main window properties."""
        self.window.attributes("-fullscreen", True)
        self._setBackground("black")
        self._cursorVisibility(False)

        # Bind keyboard and mouse events to control the screensaver.
        self.window.bind("<Motion>", self._handleMouseMotion)
        self.window.bind("<Key>", self.exit)

    def _setBackground(self, color: str):
        """Sets the background color of the window."""
        self.window.configure(background=color)
    
    def _cursorVisibility(self, status: bool):
        """Toggles the visibility of the mouse cursor."""
        if status:
            self.window.config(cursor="arrow")
        else:
            self.window.config(cursor="none")
    
    def _stopTimer(self):
        """Stops the inactivity timer."""
        if self.timer:
            self.window.after_cancel(self.timer)

    def _handleMouseMotion(self, event: tkinter.Event = None):
        """Handles mouse movement and deactivates the screensaver."""
        self._stopTimer()
        self._setBackground("#282828")
        self._cursorVisibility(True)
        self._startInactivityTimer()

    def _startInactivityTimer(self):
        """Starts the inactivity timer to trigger the screensaver."""
        self.timer = self.window.after(self.inactivityDuration, self._activateScreensaver)

    def _activateScreensaver(self):
        """Activates the screensaver mode."""
        self._cursorVisibility(False)
        self._setBackground("black")
