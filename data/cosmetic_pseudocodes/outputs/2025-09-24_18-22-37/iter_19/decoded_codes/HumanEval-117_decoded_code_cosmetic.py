from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    output_collection: List[str] = []
    split_words = string_s.split(" ")
    pos = 0
    vowels = {"a", "e", "i", "o", "u"}
    while pos < len(split_words):
        current_term = split_words[pos]
        consonant_total = 0
        char_index = 0
        while True:
            if char_index >= len(current_term):
                break
            current_char = current_term[char_index].lower()
            if current_char not in vowels and current_char.isalpha():
                consonant_total += 1
            char_index += 1
        if consonant_total == natural_number_n:
            output_collection.append(current_term)
        pos += 1
    return output_collection