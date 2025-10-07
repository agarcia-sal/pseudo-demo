from typing import List

def vowels_count(str_input: str) -> int:
    vowel_letters: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count_vowels: int = 0

    for idx in range(len(str_input)):
        ch: str = str_input[idx]
        if ch in vowel_letters:
            count_vowels += 1

    if len(str_input) > 0:
        last_char: str = str_input[-1]
        if last_char == 'y' or last_char == 'Y':
            count_vowels += 1

    return count_vowels