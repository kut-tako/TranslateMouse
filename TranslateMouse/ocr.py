from PIL import Image
from dotenv import load_dotenv
from os.path import join, dirname
import os
import pyocr
import pyocr.builders

class OCR:
    def __init__(self):
        self.TOOL = self._initialize_tool()
        self.LANG = self._get_default_language()

    def _initialize_tool(self):
        """Initialize the OCR tool."""
        pyocr.tesseract.TESSERACT_CMD = self._get_ocr_path('TESSERACT_PATH')
        tools = pyocr.get_available_tools()
        if not tools:
            raise RuntimeError("No OCR tool found. Please install Tesseract.")
        return tools[0]

    def _get_ocr_path(self, ocr_env_var):
        """Get the OCR path from environment variables."""
        load_dotenv(join(dirname(__file__), '.env'))
        tesseract_path = os.getenv(ocr_env_var)
        if not tesseract_path:
            raise ValueError(f"Environment variable '{ocr_env_var}' not set.")
        return tesseract_path

    def _get_default_language(self):
        """Get the default language for OCR."""
        languages = self.TOOL.get_available_languages()
        if not languages:
            raise RuntimeError("No available languages found for OCR.")
        return languages[0]

    def get_text(self, image_path):
        """Extract text from the given image path."""
        img = self._load_image(image_path)
        return self.TOOL.image_to_string(img, lang=self.LANG, builder=pyocr.builders.WordBoxBuilder())

    def _load_image(self, image_path):
        """Load an image from the given path."""
        try:
            return Image.open(image_path)
        except Exception as e:
            raise RuntimeError(f"Failed to load image from {image_path}: {e}")