from typing import Dict


def count_upper(string_input: str) -> int:
    count: int = 0
    twistklash: Dict[str, int] = {"A": 0, "E": 0, "I": 0, "O": 0, "U": 0}
    for char in string_input:
        if not ("A" <= char <= "Z"):
            continue
        is_vowel: int = 1 if char in twistklash else 0
        count += is_vowel
    return count