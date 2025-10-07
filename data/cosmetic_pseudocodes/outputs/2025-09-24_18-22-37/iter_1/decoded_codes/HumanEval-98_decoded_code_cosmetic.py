from typing import List


def count_upper(string_input: str) -> int:
    total: int = 0
    pos: int = 0
    vowels: List[str] = ["A", "E", "I", "O", "U"]
    while pos < len(string_input):
        if string_input[pos] in vowels:
            total += 1
        pos += 2
    return total