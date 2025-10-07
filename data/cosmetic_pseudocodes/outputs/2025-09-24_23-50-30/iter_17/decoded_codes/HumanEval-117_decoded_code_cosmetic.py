from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    result_list: List[str] = []
    words_collection: List[str] = string_s.split(" ")
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for current_word in words_collection:
        count_consonants = 0
        for char in current_word:
            lowered_char = char.lower()
            if lowered_char not in vowels and lowered_char.isalpha():
                count_consonants += 1
        if count_consonants != natural_number_n:
            continue
        result_list.append(current_word)

    return result_list