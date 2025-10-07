from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def count_consonants(text_w: str, acc_c: int, pos_i: int, len_l: int) -> int:
        if pos_i >= len_l:
            return acc_c
        current_char = text_w[pos_i].lower()
        if current_char in {'a', 'e', 'i', 'o', 'u'}:
            return count_consonants(text_w, acc_c, pos_i + 1, len_l)
        return count_consonants(text_w, acc_c + 1, pos_i + 1, len_l)

    temp_result_list: List[str] = []
    words_list = string_s.split(" ")
    idx_word = 0

    while idx_word < len(words_list):
        current_word = words_list[idx_word]
        consonant_count = count_consonants(current_word, 0, 0, len(current_word))
        if consonant_count == natural_number_n:
            temp_result_list.append(current_word)
        idx_word += 1

    return temp_result_list