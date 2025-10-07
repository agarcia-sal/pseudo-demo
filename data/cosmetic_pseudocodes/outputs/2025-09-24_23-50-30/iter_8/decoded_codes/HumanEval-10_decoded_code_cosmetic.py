from typing import Callable


def is_palindrome(input_string: str) -> bool:
    def helper(i: int, j: int) -> bool:
        while i < j:
            if input_string[i] != input_string[j]:
                return False
            i += 1
            j -= 1
        return True
    return helper(0, len(input_string) - 1)


def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""

    index_start: int
    for index_start in range(len(input_string)):
        if is_palindrome(input_string[index_start:]):
            break
    prefix = input_string[:index_start]
    suffix = ''.join(prefix[k] for k in range(len(prefix) - 1, -1, -1))
    return input_string + suffix