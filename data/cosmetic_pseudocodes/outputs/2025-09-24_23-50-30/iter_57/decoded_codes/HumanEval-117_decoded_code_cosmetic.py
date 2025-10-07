from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    collected_words: List[str] = []
    position: int = 0
    words_list = string_s.split()

    while position < len(words_list):
        current_word = words_list[position]
        consonant_count = 0
        char_idx = 0

        while char_idx < len(current_word):
            current_char = current_word[char_idx].lower()
            if current_char not in vowels:
                consonant_count += 1
            char_idx += 1

        if consonant_count == natural_number_n:
            collected_words.append(current_word)

        position += 1

    return collected_words