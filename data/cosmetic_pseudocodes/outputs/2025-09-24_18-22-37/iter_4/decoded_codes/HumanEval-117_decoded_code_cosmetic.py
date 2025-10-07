from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected_words: List[str] = []
    word_list = string_s.split(' ')
    current_word_index = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while current_word_index < len(word_list):
        current_word = word_list[current_word_index]
        consonant_count = 0
        char_pos = 0
        while char_pos < len(current_word):
            letter = current_word[char_pos].lower()
            if letter not in vowels:
                consonant_count += 1
            char_pos += 1
        if consonant_count == natural_number_n:
            collected_words.append(current_word)
        current_word_index += 1
    return collected_words