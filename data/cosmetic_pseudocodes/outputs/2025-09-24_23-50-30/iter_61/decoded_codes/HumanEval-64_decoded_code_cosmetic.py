from typing import List

def vowels_count(text_param: str) -> int:
    vowels_set: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    index_counter: int = 0
    total_vowels: int = 0

    while True:
        if not (index_counter < len(text_param)):
            break
        current_char: str = text_param[index_counter]
        if current_char in vowels_set:
            total_vowels += 1
        index_counter += 1

    last_pos: int = len(text_param) - 1
    if last_pos >= 0:
        if text_param[last_pos] in ('y', 'Y'):
            total_vowels += 1

    return total_vowels