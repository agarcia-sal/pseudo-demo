from typing import List

def vowels_count(string_input: str) -> int:
    vowel_letters: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    counter: int = 0
    index: int = 0
    while index < len(string_input):
        char: str = string_input[index]
        if char in vowel_letters:
            counter += 1
        index += 1
    if string_input and (string_input[-1] == 'y' or string_input[-1] == 'Y'):
        counter += 1
    return counter