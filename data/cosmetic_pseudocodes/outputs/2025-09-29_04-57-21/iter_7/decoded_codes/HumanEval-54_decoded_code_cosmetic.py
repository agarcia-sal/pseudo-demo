from typing import Set


def same_chars(text_a: str, text_b: str) -> bool:
    chars_a: Set[str] = set()
    chars_b: Set[str] = set()

    for character in text_a:
        chars_a.add(character)

    for element in text_b:
        chars_b.add(element)

    return not (chars_a != chars_b)