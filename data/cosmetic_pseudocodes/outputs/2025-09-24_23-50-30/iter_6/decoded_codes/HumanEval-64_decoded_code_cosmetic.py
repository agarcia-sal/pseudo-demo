from typing import List

def vowels_count(string_input: str) -> int:
    all_vowels: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count: int = 0
    index: int = 0
    while index < len(string_input):
        if string_input[index] in all_vowels:
            count += 1
        index += 1
    if string_input[-1:] in ('y', 'Y'):
        count += 1
    return count