import json

class ChineseTraditionalStrokeCounter:
    def __init__(self, stroke_data_file, list_traditional_word):
        self.stroke_data = stroke_data_file
        self.list_traditional_word = list_traditional_word

    def get_trad_stroke_count(self):
        """Lấy số nét của một mảng các ký tự tiếng Trung GIẢN THỂ.

        Args:
            list_traditional_word (list): Mảng các ký tự tiếng Trung giản thể.

        Returns:
            dict: Từ điển với key là ký tự đầu tiên trong mảng và value là số nét của ký tự đó.
        """

        list_traditional_word = self.list_traditional_word
        if not list_traditional_word:
            return {}
        result_stroke = {}
        for key in list_traditional_word:
            stroke_info = self.stroke_data.get(key)
            if stroke_info is None:
                result_stroke[key] = None
            else:
                result_stroke[key] = stroke_info[0]
            
        return result_stroke