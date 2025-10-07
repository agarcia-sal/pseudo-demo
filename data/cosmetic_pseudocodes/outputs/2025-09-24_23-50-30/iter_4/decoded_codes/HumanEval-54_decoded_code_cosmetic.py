from typing import Dict

def same_chars(string_zero: str, string_one: str) -> bool:
    charSetA: Dict[str, bool] = {}
    charSetB: Dict[str, bool] = {}
    for ch in string_zero:
        charSetA[ch] = True
    for ch in string_one:
        charSetB[ch] = True
    if len(charSetA) != len(charSetB):
        return False
    for key in charSetA:
        if key not in charSetB:
            return False
    return True