from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    output_list: List[str] = []
    words_array: List[str] = string_s.split(" ")

    def count_non_vowels(string_x: str, idx: int) -> int:
        if idx >= len(string_x):
            return 0
        ch = string_x[idx].lower()
        increment_val = 1 if ch not in {"a", "e", "i", "o", "u"} else 0
        return increment_val + count_non_vowels(string_x, idx + 1)

    for element in words_array:
        if count_non_vowels(element, 0) == natural_number_n:
            output_list.append(element)
    return output_list