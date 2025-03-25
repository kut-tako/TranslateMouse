from tkinter import *
from tkinter import ttk
import screenshot
import ocr
import translate
import win32api
import re

class Window:
    def __init__(self):
        """Initialize the main application window."""
        self.screenshot_instance = screenshot.Screenshot();
        self.translate_instance = translate.Translate();

        self.root = Tk();
        self.frame = ttk.Frame(self.root, padding=10);
        self.label = ttk.Label(self.frame, text="Initializing...");
        self.mouse_x = 0;
        self.mouse_y = 0;

        self.setup_ui();
        self.update_mouse_position();

    def setup_ui(self):
        """Set up the user interface components."""
        self.root.title("Translate Mouse");
        self.root.minsize(width=300, height=100);
        self.root.attributes('-topmost', True);
        self.frame.grid();
        self.label.grid(column=0, row=0);
        self._update_label("Waiting...");

    def main_loop(self):
        """Run the main event loop."""
        self.root.mainloop();
    
    def set_mouse_position(self, x, y):
        """Set the current mouse position."""
        self.mouse_x = x;
        self.mouse_y = y;

    def get_mouse_position(self):
        """Get the current mouse position."""
        return self.mouse_x, self.mouse_y;

    def get_mouse_position_win32(self):
        """Get the current mouse position using win32api."""
        return win32api.GetCursorPos();

    def update_mouse_position(self):
        """Update the mouse position and display it."""
        pos = self.get_mouse_position_win32();
        self.set_mouse_position(pos[0], pos[1]);
        self.root.after(50, self.update_mouse_position);

    def _update_label(self, text):
        """Update the label text."""
        self.label.config(text=text);
    
    def translate_process(self):
        """Process the translation of the text from the screenshot."""
        print("translate_process");

        img_name = self._take_screenshot();
        word_list = self._get_text_from_ocr(img_name);
        if not word_list:
            print("No text found, skipping further processing.")
            self._update_label("文字検出無し");
            return

        word = self._check_text_position(word_list);
        if not word:
            self._update_label("翻訳対象無し");
            return;

        translate_result = self._translate_word(word);
        self._update_label("翻訳結果\n" + translate_result);

    def call_translate_process(self):
        """Call the translate process."""
        self.root.after(0, self.translate_process);

    def _get_text_from_ocr(self, img_name):
        """Get the text from the OCR."""
        ocr_instance = ocr.OCR();
        return ocr_instance.get_text(img_name);

    def _take_screenshot(self):
        """Take a screenshot of the current mouse position."""
        return self.screenshot_instance.take_screenshot(self.mouse_x, self.mouse_y);

    def _check_text_position(self, text_list):
        """Check the position of the text."""
        print("text_list:", text_list);
        for text in text_list:

            if not self._is_mouse_position_between(self.mouse_x, self.mouse_y, text.position[0], text.position[1]):
                continue;
            
            word = self._search_word(text.content);
            if not word or len(word) > 1:
                continue;

            return word[0];

        return None;

    def _is_mouse_position_between(self, mouse_x, mouse_y, left_top, right_bottom):
        """Check if a value is between two other values."""
        screenshot_position = self.calculate_screenshot_position(mouse_x, mouse_y);
        screenshot_left_top_x = screenshot_position[0] + left_top[0];
        screenshot_right_bottom_x = screenshot_position[0] + right_bottom[0];
        screenshot_left_top_y = screenshot_position[1] + left_top[1];
        screenshot_right_bottom_y = screenshot_position[1] + right_bottom[1];
        return mouse_x > screenshot_left_top_x and mouse_x < screenshot_right_bottom_x and mouse_y > screenshot_left_top_y and mouse_y < screenshot_right_bottom_y;

    def calculate_screenshot_position(self, mouse_x, mouse_y):
        """Calculate the screenshot position."""
        size = self.screenshot_instance.get_size();
        return int(mouse_x - size[0] / 2), int(mouse_y - size[1] / 2);

    def _search_word(self, text):
        """Search the word from the text."""
        pattern = r'\b[a-zA-Z]+\b'
        words = re.findall(pattern, text);
        if words:
            return words;
        return None;

    def _translate_word(self, word):
        """Translate the word."""
        return self.translate_instance.translate(word);
