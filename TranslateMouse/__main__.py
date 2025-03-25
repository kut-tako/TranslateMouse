import window;
import hotkey;
import threading;

def initialize_hotkey_listener(main_window):
    """Initialize and start the hotkey listener in a separate thread."""
    hotkey_listener = hotkey.Hotkey();
    hotkey_listener.set_main_window(main_window);

    hotkey_thread = threading.Thread(target=hotkey_listener.start_listener, daemon=True);
    hotkey_thread.start();
    return hotkey_thread

def create_main_window():
    """Create and return the main application window."""
    main_window = window.Window();
    return main_window

def main():
    """Main entry point for the application."""
    main_window = create_main_window();
    initialize_hotkey_listener(main_window);
    run_main_loop(main_window);

def run_main_loop(main_window):
    """Run the main event loop for the application."""
    try:
        main_window.main_loop();
    except Exception as e:
        print(f"An error occurred during the main loop: {e}");

if __name__ == '__main__':
    main();
