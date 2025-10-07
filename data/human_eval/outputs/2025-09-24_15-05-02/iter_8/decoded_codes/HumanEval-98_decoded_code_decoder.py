from typing import Union

def count_upper(s: Union[str, bytes]) -> int:
    count: int = 0
    vowels: str = "AEIOU"
    length: int = len(s)
    for i in range(0, length, 2):
        if s[i] in vowels:
            count += 1
    return count