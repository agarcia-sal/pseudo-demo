from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    accumulator: List[str] = []
    words_array: List[str] = string_s.split(" ")
    cursor: int = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while cursor < len(words_array):
        current_item = words_array[cursor]
        count_consonants = 0
        letter_index = 0
        while letter_index < len(current_item):
            letter_lower = current_item[letter_index].lower()
            if letter_lower in vowels:
                pass  # vowel, do nothing
            else:
                count_consonants += 1
            letter_index += 1
        if count_consonants == natural_number_n:
            accumulator.append(current_item)
        cursor += 1
    return accumulator