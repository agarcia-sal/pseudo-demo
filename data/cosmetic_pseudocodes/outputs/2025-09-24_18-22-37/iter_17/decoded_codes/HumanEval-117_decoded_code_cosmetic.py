from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    output_list: List[str] = []
    word_index: int = 0
    current_terms = string_s.split(" ")
    while word_index < len(current_terms):
        term = current_terms[word_index]
        consonant_counter: int = 0
        char_position: int = 0
        while char_position <= len(term) - 1:
            letter_lower = term[char_position].lower()
            if letter_lower not in {"a", "e", "i", "o", "u"}:
                consonant_counter += 1
            char_position += 1
        if consonant_counter == natural_number_n:
            output_list.append(term)
        word_index += 1
    return output_list