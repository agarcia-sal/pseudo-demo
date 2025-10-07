from typing import Literal


def vowels_count(string_input: str) -> int:
    vowels: str = "aeiouAEIOU"
    count: int = 0

    def recursive_count(index: int) -> int:
        if index == 0:
            return 1 if string_input[0] in vowels else 0
        return (1 if string_input[index] in vowels else 0) + recursive_count(index - 1)

    if string_input:
        count = recursive_count(len(string_input) - 1)
        if string_input[-1] in ('y', 'Y'):
            count += 1

    return count