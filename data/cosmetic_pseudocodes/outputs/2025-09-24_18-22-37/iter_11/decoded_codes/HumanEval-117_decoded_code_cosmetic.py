from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    selected_words: List[str] = []
    words_list: List[str] = string_s.split(" ")

    word_cursor = 0
    while word_cursor < len(words_list):
        current_word = words_list[word_cursor]
        consonant_counter = 0

        char_pos = 0
        while char_pos < len(current_word):
            current_char = current_word[char_pos].lower()
            vowel_check = False

            if current_char in {"a", "e", "i", "o", "u"}:
                vowel_check = True

            if not vowel_check:
                consonant_counter += 1

            char_pos += 1

        if consonant_counter == natural_number_n:
            selected_words.append(current_word)

        word_cursor += 1

    return selected_words