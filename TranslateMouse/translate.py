from dotenv import load_dotenv
from os.path import join, dirname
import os
import deepl

class Translate:

    translator = None;

    def __init__(self):
        """Initialize the Translate class and load the DeepL API key."""
        self.translator = self._initialize_translator()

    def _initialize_translator(self):
        """Load the DeepL API key from the environment and return a Translator instance."""
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        auth_key = os.getenv('DEEPL_API_KEY')

        if not auth_key:
            raise ValueError("DEEPL_API_KEY not found in environment variables.")
        
        return deepl.Translator(auth_key)

    def translate(self, text, target_lang='JA'):
        """Translate the given text to the specified target language."""
        result = self.translator.translate_text(text, target_lang=target_lang)
        return result.text


