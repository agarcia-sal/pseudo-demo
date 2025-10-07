from typing import List

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_m: str, character_n: str) -> str:
        return '0' if character_m == character_n else '1'

    processed_chars: List[str] = []
    for index in range(len(string_a)):
        char_p = string_a[index]
        char_q = string_b[index]
        next_bit = xor(char_p, char_q)
        processed_chars.append(next_bit)

    return "".join(processed_chars)