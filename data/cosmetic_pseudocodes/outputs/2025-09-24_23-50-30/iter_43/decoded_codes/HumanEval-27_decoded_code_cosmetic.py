from typing import List

def flip_case(param_xz: str) -> str:
    array_o: List[str] = []
    integer_j: int = 0

    while integer_j < len(param_xz):
        char_c: str = param_xz[integer_j]
        if 'a' <= char_c <= 'z':
            char_c = chr(ord(char_c) - (ord('a') - ord('A')))
        elif 'A' <= char_c <= 'Z':
            char_c = chr(ord(char_c) + (ord('a') - ord('A')))
        # else char_c unchanged
        array_o.append(char_c)
        integer_j += 1

    return ''.join(array_o)