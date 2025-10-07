from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    output_list: List[str] = []
    word_list = string_s.split(" ")
    for current_word in word_list:
        consonant_tally = sum(
            1 for ch in current_word if ch.lower() not in vowels
        )
        if consonant_tally == natural_number_n:
            output_list.append(current_word)
    return output_list