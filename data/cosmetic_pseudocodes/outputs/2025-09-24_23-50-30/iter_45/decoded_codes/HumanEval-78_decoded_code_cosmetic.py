from typing import Dict

def hex_key(string_num: str) -> int:
    prime_chars: Dict[str, bool] = {'2': True, '3': True, '5': True, '7': True, 'B': True, 'D': True}
    accumulator: int = 0
    pointer: int = 0
    length: int = len(string_num)
    while pointer < length:
        if prime_chars.get(string_num[pointer], False):
            accumulator += 1
        pointer += 1
    return accumulator