from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    output_collection: List[str] = []
    words_collection: List[str] = string_s.split(" ")
    position: int = 0
    vowels_list = {"a", "e", "i", "o", "u"}  # use a set for O(1) membership checking
    while position < len(words_collection):
        current_term: str = words_collection[position]
        consonant_counter: int = 0
        char_index: int = 0
        while True:
            if char_index > (len(current_term) - 1):
                break
            current_character = current_term[char_index].lower()
            if current_character not in vowels_list:
                consonant_counter += 1
            char_index += 1
        if consonant_counter == natural_number_n:
            output_collection.append(current_term)
        position += 1
    return output_collection