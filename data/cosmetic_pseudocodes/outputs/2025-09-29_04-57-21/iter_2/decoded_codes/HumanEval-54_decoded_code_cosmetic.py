from typing import List

def same_chars(string_zero: str, string_one: str) -> bool:
    zero_chars: List[str] = []
    one_chars: List[str] = []
    for char in string_zero:
        if char not in zero_chars:
            zero_chars.append(char)
    for char in string_one:
        if char not in one_chars:
            one_chars.append(char)
    zero_chars.sort()
    one_chars.sort()
    if len(zero_chars) == len(one_chars):
        index: int = 0
        while index < len(zero_chars):
            if zero_chars[index] != one_chars[index]:
                return False
            index += 1
        return True
    else:
        return False