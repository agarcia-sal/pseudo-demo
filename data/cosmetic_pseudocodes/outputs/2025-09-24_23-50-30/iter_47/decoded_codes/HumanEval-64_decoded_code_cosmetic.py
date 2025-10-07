from typing import List


def vowels_count(string_input: str) -> int:
    reference_vowels: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    tally_vowels: int = 0
    for index_cursor in range(len(string_input)):
        if string_input[index_cursor] in reference_vowels:
            tally_vowels += 1

    if string_input[-1:] in ('y', 'Y'):
        tally_vowels += 1

    return tally_vowels