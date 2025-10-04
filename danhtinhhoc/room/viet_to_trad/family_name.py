import json

class VietnameseFamilyNameConverter:
    def __init__(self, json_file, family_name):
        """Khởi tạo đối tượng chuyển đổi tên.

        Args:
            json_file_path (str): Đường dẫn đến file JSON chứa ánh xạ họ tiếng Việt - chữ Hán.
        """
        self.json_file = json_file
        self.family_name = family_name

    def to_traditional(self):
        """Chuyển đổi họ tiếng Việt sang chữ Hán.

        Args:
            family_name (str): Họ tiếng Việt.

        Returns:
            str: Tên traditional (chữ Hán) tương ứng.
            None: Nếu không tìm thấy.
        """
        traditional_name_result = {}
        family_name = self.family_name
        for name in family_name:
            traditional_name = self.json_file.get(name)
            if traditional_name is None:
                print(f"Không tìm thấy tên traditional cho họ {name}")
            else:
                traditional_name_result[name] = traditional_name
        return traditional_name_result