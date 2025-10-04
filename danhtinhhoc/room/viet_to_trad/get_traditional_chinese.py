import json

class compare_and_filter:
    def __init__(self, converter_result, lookup_result):
        self.converter_result = converter_result  # Không cần dấu gạch dưới __
        self.lookup_result = lookup_result        # Không cần dấu gạch dưới __

    def compare_and_filter_result(self):
        """
        So sánh và lọc kết quả từ hai lớp VietnameseToChineseConverter và ChineseNameLookup.

        Returns:
            Từ điển với key là từ tiếng Việt và value là danh sách các kết hợp chữ Hán đã được lọc và tính phần trăm.
        """
        filtered_result = {}
        for word, data in self.lookup_result.items():  # Sử dụng self.lookup_result
            traditional_matches = self.converter_result.get(word, {}).get('traditional', [])
            filtered_matches = [
                [item[0], item[1]] for item in data if item[0] in traditional_matches
            ]

            # Tính phần trăm và sắp xếp
            if filtered_matches:
                total_count = sum(item[1] for item in filtered_matches)  # Tổng số lần xuất hiện
                for item in filtered_matches:
                    item[1] = round((item[1] / total_count) * 100, 3)  # Tính phần trăm
                filtered_matches.sort(key=lambda x: -x[1])  # Sắp xếp giảm dần
                filtered_result[word] = filtered_matches  # Lưu vào filtered_result

        return filtered_result
