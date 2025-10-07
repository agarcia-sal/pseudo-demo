from typing import Union

def count_upper(string_s: str) -> int:
    count: int = 0
    length: int = len(string_s)
    for index in range(0, length, 2):
        char: str = string_s[index]
        if char in "AEIOU":
            count += 1
    return count