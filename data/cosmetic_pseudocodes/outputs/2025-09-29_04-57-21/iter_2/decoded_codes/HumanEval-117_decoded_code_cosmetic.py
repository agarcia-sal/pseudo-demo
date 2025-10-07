from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels_set = {"a", "e", "i", "o", "u"}
    filtered_words: List[str] = []
    separated_words = string_s.split(" ")

    for current_word in separated_words:
        consonant_counter = 0
        char_index = 0

        while char_index < len(current_word):
            letter_lower = current_word[char_index].lower()
            if letter_lower not in vowels_set:
                consonant_counter += 1
            char_index += 1

        if consonant_counter == natural_number_n:
            filtered_words.append(current_word)

    return filtered_words