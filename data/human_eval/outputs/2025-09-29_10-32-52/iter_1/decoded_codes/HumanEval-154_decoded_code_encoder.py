from typing import Union


def cycpattern_check(string_a: str, string_b: str) -> bool:
    length_of_b: int = len(string_b)
    pattern: str = string_b + string_b
    max_index_i: int = len(string_a) - length_of_b
    for index_i in range(max_index_i + 1):
        for index_j in range(length_of_b + 1):
            if string_a[index_i : index_i + length_of_b] == pattern[index_j : index_j + length_of_b]:
                return True
    return False