from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    result_list: List[str] = []
    word_collection: List[str] = string_s.split(" ")
    index_ptr: int = 0
    vowel_set = {"a", "e", "i", "o", "u"}

    while index_ptr < len(word_collection):
        current_word = word_collection[index_ptr]
        consonant_counter = 0
        char_pos = 0
        while char_pos != len(current_word):
            current_char = current_word[char_pos].lower()
            if current_char not in vowel_set:
                consonant_counter += 1
            char_pos += 1
        if consonant_counter == natural_number_n:
            result_list.append(current_word)
        index_ptr += 1

    return result_list