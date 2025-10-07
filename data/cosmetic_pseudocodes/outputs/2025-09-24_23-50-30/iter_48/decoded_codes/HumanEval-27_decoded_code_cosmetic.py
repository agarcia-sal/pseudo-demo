from typing import List

def flip_case(data_string: str) -> str:
    out_chars: List[str] = []
    idx: int = 0
    while idx < len(data_string):
        current_char: str = data_string[idx]
        if 'a' <= current_char <= 'z':
            out_chars.append(chr(ord(current_char) - (ord('a') - ord('A'))))
        elif 'A' <= current_char <= 'Z':
            out_chars.append(chr(ord(current_char) + (ord('a') - ord('A'))))
        else:
            out_chars.append(current_char)
        idx += 1
    return ''.join(out_chars)