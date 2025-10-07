from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    filtered_list: List[str] = []
    word_list: List[str] = string_s.split(" ")
    vowel_collection: List[str] = ["a", "e", "i", "o", "u"]

    word_index: int = 0
    while word_index < len(word_list):
        current_word: str = word_list[word_index]
        consonant_counter: int = 0
        pos: int = 0

        while pos < len(current_word):
            current_char_lower: str = current_word[pos].lower()
            if current_char_lower not in vowel_collection:
                consonant_counter += 1
            pos += 1

        if consonant_counter == natural_number_n:
            filtered_list.append(current_word)

        word_index += 1

    return filtered_list