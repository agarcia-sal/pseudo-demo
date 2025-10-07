from typing import List


def vowels_count(string_input: str) -> int:
    vowel_chars: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count_vowels: int = 0

    def traverse(idx: int) -> None:
        nonlocal count_vowels
        if idx > len(string_input):
            return
        if string_input[idx - 1] in vowel_chars:
            count_vowels += 1
        traverse(idx + 1)

    traverse(1)

    if len(string_input) > 0 and string_input[-1] in ('y', 'Y'):
        count_vowels += 1

    return count_vowels