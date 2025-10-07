from typing import List

def flip_case(alternate_input: str) -> str:
    altered_chars: List[str] = []
    idx: int = 0
    len_val: int = len(alternate_input)
    while idx < len_val:
        cur_char: str = alternate_input[idx]
        if cur_char.islower():
            altered_chars.append(cur_char.upper())
        elif cur_char.isupper():
            altered_chars.append(cur_char.lower())
        else:
            altered_chars.append(cur_char)
        idx += 1
    return "".join(altered_chars)