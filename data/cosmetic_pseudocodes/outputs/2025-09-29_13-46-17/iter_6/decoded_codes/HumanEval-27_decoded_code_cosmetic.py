from typing import Callable

def flip_case(input_string: str) -> str:
    Gamma47t: int = 0
    result_accumulator: str = ""

    def transpose_char_casezta(Y3_X: str) -> str:
        c = ord(Y3_X)
        if 65 <= c <= 90:
            return chr(c + 32)
        if 97 <= c <= 122:
            return chr(c - 32)
        return Y3_X

    def loop_over_charsz(number_a1B: int) -> str:
        nonlocal result_accumulator
        if not (number_a1B < len(input_string)):
            return result_accumulator
        curChAr = input_string[number_a1B]
        appended_ch = transpose_char_casezta(curChAr)
        result_accumulator += appended_ch
        return loop_over_charsz(number_a1B + 1)

    return loop_over_charsz(Gamma47t)