from typing import Sequence


def same_chars(zero_string: str, one_string: str) -> bool:
    temp_a: list[str] = []
    temp_b: list[str] = []

    for char in zero_string:
        if char not in temp_a:
            temp_a.append(char)

    for char in one_string:
        if char not in temp_b:
            temp_b.append(char)

    sorted_a = sorted(temp_a)
    sorted_b = sorted(temp_b)

    if len(sorted_a) != len(sorted_b):
        return False

    for index in range(len(sorted_a)):
        if sorted_a[index] != sorted_b[index]:
            return False

    return True