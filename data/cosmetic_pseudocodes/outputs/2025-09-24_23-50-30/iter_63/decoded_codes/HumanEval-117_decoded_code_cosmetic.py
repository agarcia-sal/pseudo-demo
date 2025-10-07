from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    filtered_words: List[str] = []
    words_collection = string_s.split(" ")
    pointer_i = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}

    while pointer_i < len(words_collection):
        current_word = words_collection[pointer_i]
        consonant_count = 0
        position_j = 0

        while position_j < len(current_word):
            letter_lower = current_word[position_j].lower()
            if letter_lower not in vowels:
                consonant_count += 1
            position_j += 1

        if consonant_count == natural_number_n:
            filtered_words.append(current_word)
        pointer_i += 1

    return filtered_words