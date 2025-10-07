from typing import Callable


def vowels_count(parameter_string: str) -> int:
    lookup_vowels: str = "AEIOUaeiou"

    def count_helper(index: int, acc: int) -> int:
        if index < 0:
            return acc
        current_char = parameter_string[index]
        updated_acc = acc + (1 if current_char in lookup_vowels else 0)
        return count_helper(index - 1, updated_acc)

    total_vowels: int = count_helper(len(parameter_string) - 1, 0)

    if len(parameter_string) > 0 and parameter_string[-1] in ('y', 'Y'):
        total_vowels += 1

    return total_vowels