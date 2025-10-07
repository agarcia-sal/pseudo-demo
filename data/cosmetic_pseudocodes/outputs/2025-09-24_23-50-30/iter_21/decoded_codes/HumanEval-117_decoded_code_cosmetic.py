from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def count_consonants(word_input: str) -> int:
        count_consonants_local = 0
        for char_element in word_input:
            lowered_char = char_element.lower()
            if lowered_char in {'a', 'e', 'i', 'o', 'u'}:
                continue
            # Count only alphabetic consonants
            if lowered_char.isalpha():
                count_consonants_local += 1
        return count_consonants_local

    return [word_item for word_item in string_s.split(" ") if count_consonants(word_item) == natural_number_n]