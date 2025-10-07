from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(inner_m: str, inner_n: str) -> str:
        # Return '0' if characters are equal, else '1'
        comparison_flag: bool = (inner_m == inner_n)
        return '0' if comparison_flag else '1'

    concatenated_result: str = ""
    index_p: int = 0
    length_q: int = len(string_a)

    while index_p < length_q:
        char_alpha: str = string_a[index_p]
        char_beta: str = string_b[index_p]
        xor_val: str = xor(char_alpha, char_beta)
        concatenated_result += xor_val
        index_p += 1

    return concatenated_result