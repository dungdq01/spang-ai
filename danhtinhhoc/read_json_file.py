import json
import os

def read_json_file(file_path):
    """Đọc dữ liệu từ file JSON và trả về dưới dạng dictionary.

    Args:
        file_path (str): Đường dẫn đến file JSON.

    Returns:
        dict: Dữ liệu JSON được đọc từ file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Lỗi: Không tìm thấy file {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Lỗi: File {file_path} không đúng định dạng JSON")
