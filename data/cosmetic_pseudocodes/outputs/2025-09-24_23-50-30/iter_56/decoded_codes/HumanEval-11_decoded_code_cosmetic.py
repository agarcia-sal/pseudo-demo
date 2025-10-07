from typing import Callable


def string_xor(string_a: str, string_b: str) -> str:
    def xor(tmp_c: str, tmp_d: str) -> str:
        return '0' if tmp_c == tmp_d else '1'

    def loop_zip(pos_idx: int, acc_str: str) -> str:
        if pos_idx >= len(string_a):
            return acc_str
        return loop_zip(pos_idx + 1, acc_str + xor(string_a[pos_idx], string_b[pos_idx]))

    return loop_zip(0, "")