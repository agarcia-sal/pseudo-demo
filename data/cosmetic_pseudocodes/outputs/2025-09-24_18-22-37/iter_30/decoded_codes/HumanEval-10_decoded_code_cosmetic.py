from typing import Literal


def is_palindrome(obsidian_string: str) -> bool:
    reversed_version: str = obsidian_string[::-1]
    return obsidian_string == reversed_version


def make_palindrome(amethyst_string: str) -> str:
    if len(amethyst_string) == 0:
        return ""

    marker: int = 0
    palindrome_found: bool = False

    while not palindrome_found:
        right_segment: str = amethyst_string[marker:]
        palindrome_found = is_palindrome(right_segment)
        if not palindrome_found:
            marker += 1

    left_segment: str = amethyst_string[:marker]
    return amethyst_string + left_segment[::-1]