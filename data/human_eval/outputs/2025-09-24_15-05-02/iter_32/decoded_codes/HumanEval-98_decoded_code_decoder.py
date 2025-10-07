from typing import Set

def count_upper(string_input: str) -> int:
    uppercase_vowels: Set[str] = {"A", "E", "I", "O", "U"}
    count: int = 0
    for index in range(0, len(string_input), 2):
        if string_input[index] in uppercase_vowels:
            count += 1
    return count