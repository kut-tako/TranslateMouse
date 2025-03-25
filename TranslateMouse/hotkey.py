from pynput import keyboard;

class Hotkey:

    pressed_keys = None;
    listener = None;
    hotkey = None;
    main_window = None;

    def __init__(self):
        """Initialize the Hotkey class and set the default hotkey."""
        self.pressed_keys = set();
        self.hotkey = keyboard.HotKey(
            keyboard.HotKey.parse('<shift>+a'),
            self.on_activate
        )
        self.listener = None;
        self.main_window = None;

    def set_hotkey(self, hotkey):
        """Set a new hotkey."""
        self.hotkey = hotkey;

    def get_hotkey(self):
        """Get the current hotkey."""
        return self.hotkey;

    def set_main_window(self, main_window):
        """Set the main window instance."""
        self.main_window = main_window;

    def get_main_window(self):
        """Get the main window instance."""
        return self.main_window;

    def on_activate(self):
        """Action to perform when the hotkey is activated."""
        print("Hotkey activated!")
        if self.main_window:
            self.main_window.call_translate_process();

    def _for_canonical(self, f):
        """Return a function that canonicalizes the key."""
        return lambda k: f(self.listener.canonical(k))

    def start_listener(self):
        """Start the keyboard listener."""
        with keyboard.Listener(
            on_press=self._for_canonical(self.hotkey.press),
            on_release=self._for_canonical(self.hotkey.release)) as self.listener:
            self.listener.join()

    def stop_listener(self):
        """Stop the keyboard listener if it is running."""
        if self.listener:
            self.listener.stop()
            self.listener = None
