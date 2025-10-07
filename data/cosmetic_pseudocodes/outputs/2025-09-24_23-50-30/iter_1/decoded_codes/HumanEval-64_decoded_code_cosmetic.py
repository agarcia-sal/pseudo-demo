from typing import List

def vowels_count(string_input: str) -> int:
    vowels_list: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count: int = 0
    index: int = 0
    length: int = len(string_input)
    while index < length:
        current_char: str = string_input[index]
        if current_char in vowels_list:
            count += 1
        index += 1
    if length > 0:
        last_char: str = string_input[length - 1]
        if last_char in ('y', 'Y'):
            count += 1
    return count