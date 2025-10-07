from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    list_y: List[str] = string_s.split(" ")
    list_z: List[str] = []

    def count_consonants(list_a: str, number_b: int, index_c: int) -> int:
        if index_c == len(list_a):
            return number_b
        else:
            char_d = list_a[index_c].lower()
            if char_d in {"a", "e", "i", "o", "u"}:
                return count_consonants(list_a, number_b, index_c + 1)
            else:
                return count_consonants(list_a, number_b + 1, index_c + 1)

    def process_words(list_e: List[str], list_f: List[str], idx_g: int) -> List[str]:
        if idx_g == len(list_e):
            return list_f
        else:
            current_word_h = list_e[idx_g]
            consonant_count_i = count_consonants(current_word_h, 0, 0)
            if consonant_count_i == natural_number_n:
                return process_words(list_e, list_f + [current_word_h], idx_g + 1)
            else:
                return process_words(list_e, list_f, idx_g + 1)

    return process_words(list_y, list_z, 0)