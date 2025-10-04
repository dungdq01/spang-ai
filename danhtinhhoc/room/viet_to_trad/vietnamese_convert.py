import json
import os

class VietnameseToChineseConverter:
    def __init__(self, vietnamese_words, vn_to_simp, simp_to_trad):
        self.vietnamese_words = vietnamese_words
        self.vn_to_simp = vn_to_simp
        self.simp_to_trad = simp_to_trad

    def find_simplified_words(self):
        output = []
        for word in self.vietnamese_words:
            word  =  word.lower()
            simplified = self.vn_to_simp.get(word, [])
            if not simplified:
                print(f"Không tìm thấy từ '{word}' trong từ điển.")
            output.append(simplified)
        return output

    def find_traditional_words(self, simplified_words):
        trad_output = []
        for simp_word in simplified_words:
            trad_words = []
            for simp in simp_word:
                trad_words.extend(self.simp_to_trad.get(simp, []))
            trad_output.append(trad_words)
        return trad_output

    def combine_words(self, word_lists):
        if not word_lists:
            return []

        def backtrack(index, current_combination):
            if index == len(word_lists):
                result.append(''.join(current_combination))
                return

            for word in word_lists[index]:
                backtrack(index + 1, current_combination + [word])

        result = []
        backtrack(0, [])
        return result

    def convert_words(self):
        result = {}
        simplified_words = self.find_simplified_words()
        for i, word in enumerate(self.vietnamese_words):
            if simplified_words[i]:
                simplified_combinations = self.combine_words([simplified_words[i]])
                traditional_words = self.find_traditional_words([simplified_words[i]])
                traditional_combinations = self.combine_words(traditional_words)
                result[word] = {
                    'simplified': simplified_combinations,
                    'traditional': traditional_combinations
                }
        return result
    
