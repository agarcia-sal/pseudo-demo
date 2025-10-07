from typing import Union

def count_upper(string_s: str) -> int:
    count: int = 0
    vowels: str = "AEIOU"
    for i in range(0, len(string_s), 2):
        if string_s[i] in vowels:
            count += 1
    return count