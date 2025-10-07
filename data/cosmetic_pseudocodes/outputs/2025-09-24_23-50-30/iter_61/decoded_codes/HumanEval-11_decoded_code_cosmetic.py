from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_o: str, character_p: str) -> str:
        if character_o != character_p:
            return '1'
        else:
            return '0'

    def loop_over_tuple(index_q: int, accumulated_r: str) -> str:
        if index_q >= len(string_a):
            return accumulated_r
        pair_s = (string_a[index_q], string_b[index_q])
        new_char_t = xor(pair_s[0], pair_s[1])
        return loop_over_tuple(index_q + 1, accumulated_r + new_char_t)

    return loop_over_tuple(0, "")