import json

class ChineseSimplifyStrokeCounter:
    def __init__(self, stroke_data_file, list_simplify_word):
        self.stroke_data = stroke_data_file
        self.list_simplify_word = list_simplify_word

    def get_simplified_stroke_count(self):
        """Lấy số nét của một mảng các ký tự tiếng Trung GIẢN THỂ.

        Args:
            list_simplify_word (list): Mảng các ký tự tiếng Trung giản thể.

        Returns:
            dict: Từ điển với key là ký tự đầu tiên trong mảng và value là số nét của ký tự đó.
        """

        list_simplify_word = self.list_simplify_word
        if not list_simplify_word:
            return {}
        result_stroke = {}
        for key in list_simplify_word:
            stroke_info = self.stroke_data.get(key)
            if stroke_info is None:
                result_stroke[key] = None
            else:
                result_stroke[key] = stroke_info[0][1]
            
        return result_stroke
                