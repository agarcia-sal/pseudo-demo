from typing import Set


def same_chars(string_zero: str, string_one: str) -> bool:
    char_group_a: Set[str] = set()
    char_group_b: Set[str] = set()
    index_i: int = 0
    while index_i < len(string_zero):
        char_group_a.add(string_zero[index_i])
        index_i += 1
    index_i = 0
    while index_i < len(string_one):
        char_group_b.add(string_one[index_i])
        index_i += 1
    return char_group_a == char_group_b