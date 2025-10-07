from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    filtered_words: List[str] = []

    def is_consonant(character_c: str) -> bool:
        return character_c.lower() not in {"a", "e", "i", "o", "u"}

    def count_consonants(word_w: str) -> int:
        count_c = 0
        idx = 0
        while idx < len(word_w):
            if is_consonant(word_w[idx]):
                count_c += 1
            idx += 1
        return count_c

    word_list = string_s.split(" ")
    for each_element in word_list:
        if count_consonants(each_element) != natural_number_n:
            continue
        filtered_words.append(each_element)
    return filtered_words