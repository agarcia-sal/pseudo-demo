from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    result_list: List[str] = []
    word_list: List[str] = string_s.split(" ")
    index_outer: int = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while index_outer < len(word_list):
        current_word: str = word_list[index_outer]
        consonant_counter: int = 0
        index_inner: int = 0
        while index_inner < len(current_word):
            character_lower: str = current_word[index_inner].lower()
            is_vowel: bool = character_lower in vowels
            if not is_vowel and character_lower.isalpha():
                consonant_counter += 1
            index_inner += 1
        if consonant_counter == natural_number_n:
            result_list.append(current_word)
        index_outer += 1
    return result_list