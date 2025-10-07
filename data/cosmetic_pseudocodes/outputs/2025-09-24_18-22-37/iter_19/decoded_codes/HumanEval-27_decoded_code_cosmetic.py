from typing import List

def flip_case(para_string: str) -> str:
    toggled_chars: List[str] = []
    idx: int = 0
    while idx < len(para_string):
        char_val: str = para_string[idx]
        if 'A' <= char_val <= 'Z':
            toggled_chars.append(chr(ord(char_val) + 32))
        elif 'a' <= char_val <= 'z':
            toggled_chars.append(chr(ord(char_val) - 32))
        else:
            toggled_chars.append(char_val)
        idx += 1
    return ''.join(toggled_chars)