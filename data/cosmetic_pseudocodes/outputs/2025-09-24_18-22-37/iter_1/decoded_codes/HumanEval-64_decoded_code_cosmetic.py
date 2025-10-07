from typing import List


def vowels_count(string_input: str) -> int:
    vowels_list: List[str] = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    count: int = 0
    for char in string_input:
        if char in vowels_list:
            count += 1
    if string_input and string_input[-1] in ('y', 'Y'):
        count += 1
    return count