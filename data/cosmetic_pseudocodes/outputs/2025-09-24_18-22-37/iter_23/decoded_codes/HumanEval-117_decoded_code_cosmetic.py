from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected_words: List[str] = []
    words_in_string: List[str] = string_s.split(" ")
    word_iter_index: int = 0
    vowels_list: List[str] = ["a", "e", "i", "o", "u"]
    while word_iter_index < len(words_in_string):
        current_word: str = words_in_string[word_iter_index]
        consonant_count: int = 0
        char_pos: int = 0
        while char_pos < len(current_word):
            current_letter: str = current_word[char_pos].lower()
            if all(current_letter != vowel for vowel in vowels_list):
                consonant_count += 1
            char_pos += 1
        if consonant_count == natural_number_n:
            collected_words.append(current_word)
        word_iter_index += 1
    return collected_words