def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_p: str, character_q: str) -> str:
        return '0' if character_p == character_q else '1'

    length_n: int = len(string_a)
    accumulated_result: str = ""
    iterator_m: int = 0

    while iterator_m < length_n:
        char_left: str = string_a[iterator_m]
        char_right: str = string_b[iterator_m]
        xor_res: str = xor(char_left, char_right)
        accumulated_result += xor_res
        iterator_m += 1

    return accumulated_result