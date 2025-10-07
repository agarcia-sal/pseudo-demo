from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected_words: List[str] = []
    words_list: List[str] = string_s.split(" ")
    word_cursor: int = 0
    while word_cursor < len(words_list):
        current_word: str = words_list[word_cursor]
        consonant_counter: int = 0
        char_position: int = 0
        while char_position < len(current_word) - 1:
            character_lower: str = current_word[char_position].lower()
            vowel_candidates: List[str] = ["a", "e", "i", "o", "u"]
            is_consonant: bool = (
                character_lower != vowel_candidates[0]
                and character_lower != vowel_candidates[1]
                and character_lower != vowel_candidates[2]
                and character_lower != vowel_candidates[3]
                and character_lower != vowel_candidates[4]
            )
            if is_consonant:
                consonant_counter += 1
            char_position += 1
        if consonant_counter == natural_number_n:
            collected_words.append(current_word)
        word_cursor += 1
    return collected_words