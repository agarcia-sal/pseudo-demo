from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    output_list: List[str] = []
    words_collection: List[str] = string_s.split(" ")
    current_index: int = 0
    vowels = {"a", "e", "i", "o", "u"}
    while current_index < len(words_collection):
        current_word = words_collection[current_index]
        consonant_counter = 0
        char_pos = 0
        while char_pos <= len(current_word) - 1:
            char_lower = current_word[char_pos].lower()
            if char_lower not in vowels:
                consonant_counter += 1
            char_pos += 1
        if consonant_counter == natural_number_n:
            output_list.append(current_word)
        current_index += 1
    return output_list