from itertools import product

from itertools import product

class ChineseNameLookup:
    def __init__(self, vietnamese_words, total_dictionary,key="chinese_text"):
        self.vietnamese_words = vietnamese_words
        self.total_dictionary = total_dictionary
        self.key = key

    def lookup(self):
        """
        Tìm kiếm các kết hợp chữ Hán cho từng từ tiếng Việt trong danh sách.

        Args:
            key: Key để lấy giá trị chữ Hán từ từ điển (mặc định là "chinese_text").

        Returns:
            Chuỗi JSON với key là từ tiếng Việt và value là danh sách các kết hợp chữ Hán đã sắp xếp theo tần suất giảm dần.
        """
        key = self.key
        result = {}
        for word in self.vietnamese_words:
            name_split = [name.lower().strip() for name in word.split(' ')]
            possible_translations = [self.total_dictionary[name] for name in name_split if name in self.total_dictionary]
            all_combinations = list(product(*possible_translations))
            word_result = []
            for combination in all_combinations:
                combined_name = ''.join([item[key] for item in combination])
                frequency_product = 1
                for item in combination:
                    frequency_product *= (int(item['freq']) + 1)
                word_result.append([combined_name, frequency_product**(1/len(word))])
            word_result.sort(key=lambda x: -x[1])
            result[word] = word_result
        return result