from typing import Union

def digitSum(s: str) -> int:
    if s == "":
        return 0
    total: int = 0
    for char in s:
        if char.isupper():
            total += ord(char)
    return total