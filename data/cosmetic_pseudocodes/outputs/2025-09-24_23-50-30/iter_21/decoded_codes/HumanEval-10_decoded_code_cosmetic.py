from typing import Callable


def is_palindrome(input_string: str) -> bool:
    indexA: int = 0
    indexB: int = len(input_string) - 1
    while indexA < indexB:
        if input_string[indexA] != input_string[indexB]:
            return False
        indexA += 1
        indexB -= 1
    return True


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""

    def find_suffix_start(current_index: int) -> int:
        if current_index == len(input_string):
            return current_index
        elif is_palindrome(input_string[current_index:]):
            return current_index
        else:
            return find_suffix_start(current_index + 1)

    split_point: int = find_suffix_start(0)
    prefix: str = input_string[:split_point]
    reversed_prefix: str = ""

    i: int = len(prefix) - 1
    while i >= 0:
        reversed_prefix += prefix[i]
        i -= 1

    return input_string + reversed_prefix