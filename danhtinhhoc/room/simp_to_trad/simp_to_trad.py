import json
import os

class SimplifiedToTraditionalConverter:
    """Converts Simplified Chinese text to Traditional Chinese using a mapping file."""

    def __init__(self, mapping_file_path=None):
        """
        Initializes the converter and loads the mapping dictionary.

        Args:
            mapping_file_path (str, optional): The path to the simp_to_trad.json file.
                                               If None, it constructs a default path.
        """
        if mapping_file_path is None:
            # Construct the path to 'danhtinhhoc/room/cabinet/simp_to_trad.json'
            # This assumes the script is run from the project root.
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            mapping_file_path = os.path.join(base_dir, 'room', 'cabinet', 'simp_to_trad.json')

        try:
            with open(mapping_file_path, 'r', encoding='utf-8') as f:
                self.mapping = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Mapping file not found at {mapping_file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON from {mapping_file_path}")

    def convert(self, text):
        """
        Converts a string from Simplified to Traditional Chinese.

        Args:
            text (str): The Simplified Chinese string to convert.

        Returns:
            str: The converted Traditional Chinese string.
        """
        if not isinstance(text, str):
            return text

        traditional_chars = []
        for char in text:
            # Look up the character in the mapping
            # If found, use the first corresponding traditional character
            # If not found, keep the original character
            traditional_char_list = self.mapping.get(char)
            if traditional_char_list:
                traditional_chars.append(traditional_char_list[0])
            else:
                traditional_chars.append(char)
        
        return "".join(traditional_chars)
