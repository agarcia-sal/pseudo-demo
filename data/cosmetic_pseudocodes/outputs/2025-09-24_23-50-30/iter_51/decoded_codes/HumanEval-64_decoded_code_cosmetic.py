from typing import Callable


def vowels_count(from_string: str) -> int:
    vowels_set = "AEIOUaeiou"

    def count_vowels_at(index: int, acc: int) -> int:
        if index == len(from_string):
            return acc
        return count_vowels_at(index + 1, acc + (1 if from_string[index] in vowels_set else 0))

    total = count_vowels_at(1, 0)

    last_idx = len(from_string)
    last_char = from_string[last_idx - 1] if last_idx > 0 else ""
    if not (last_char != "y" and last_char != "Y"):
        total += 1

    return total