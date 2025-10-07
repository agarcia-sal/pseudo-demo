from typing import Set


def same_chars(text_a: str, text_b: str) -> bool:
    set_a: Set[str] = set()
    index: int = 0
    while index < len(text_a):
        set_a.add(text_a[index])
        index += 1

    set_b: Set[str] = set()
    for idx in range(len(text_b)):
        set_b.add(text_b[idx])

    return set_a == set_b