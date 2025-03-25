import mss;

class Screenshot:
    DEFAULT_WIDTH = 250;
    DEFAULT_HEIGHT = 100;

    def __init__(self, width = DEFAULT_WIDTH, height = DEFAULT_HEIGHT):
        """Initialize the screenshot."""
        self.width = width;
        self.height = height;

    def set_size(self, width, height):
        """Set the size of the screenshot."""
        self.width = width;
        self.height = height;
    
    def get_size(self):
        """Get the size of the screenshot."""
        return self.width, self.height;

    def take_screenshot(self, left = 0, top = 0, width = None, height = None, output_path = "screenshot.png"):
        """Take a screenshot of the specified area."""
        width = width or self.width;
        height = height or self.height;

        with mss.mss() as sct:
            bbox = self._calculate_bbox(left, top, width, height)
            img = sct.grab(bbox)
            return self._save_screenshot(img, output_path)

    def _calculate_bbox(self, left, top, width, height):
        """Calculate the bounding box for the screenshot."""
        left = int(left - width / 2);
        right = left + width;
        top = int(top - height / 2);
        bottom = top + height;
        return (left, top, right, bottom)

    def _save_screenshot(self, img, output_path):
        """Save the screenshot to a specified file."""
        try:
            mss.tools.to_png(img.rgb, img.size, output=output_path)
            return output_path
        except Exception as e:
            print(f"Error saving screenshot: {e}")
            return None

