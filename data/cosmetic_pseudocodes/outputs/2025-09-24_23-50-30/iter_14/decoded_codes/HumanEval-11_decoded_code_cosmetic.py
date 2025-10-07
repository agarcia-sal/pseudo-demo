from typing import List


def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_1: str, char_2: str) -> str:
        return '1' if char_1 != char_2 else '0'

    output_chars: List[str] = [xor(string_a[idx], string_b[idx]) for idx in range(len(string_a))]
    return ''.join(output_chars)