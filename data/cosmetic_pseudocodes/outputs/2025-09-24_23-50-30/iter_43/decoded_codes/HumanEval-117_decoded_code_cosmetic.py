from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    result: List[str] = []
    array_words = string_s.split(" ")
    index_i = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while index_i < len(array_words):
        word_x = array_words[index_i]
        count_y = 0
        position_p = 0
        while position_p < len(word_x):
            char_c = word_x[position_p].lower()
            if char_c in vowels:
                position_p += 1
                continue
            else:
                count_y += 1
                position_p += 1
        if count_y == natural_number_n:
            result.append(word_x)
        index_i += 1
    return result