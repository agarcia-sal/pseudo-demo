from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    output: List[str] = []
    words_list: List[str] = string_s.split(" ")
    current_index: int = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while current_index < len(words_list):
        target_word = words_list[current_index]
        consonant_accumulator = 0
        char_pos = 0
        while char_pos < len(target_word):
            character_lower = target_word[char_pos].lower()
            if character_lower not in vowels:
                consonant_accumulator += 1
            char_pos += 1
        if consonant_accumulator == natural_number_n:
            output.append(target_word)
        current_index += 1
    return output