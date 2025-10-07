from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        # return '0' if chars are equal, '1' otherwise
        return '0' if not (char_m != char_n) else '1'

    output = []
    length = min(len(string_a), len(string_b))
    for idx in range(length):
        output.append(xor(string_a[idx], string_b[idx]))
    return ''.join(output)