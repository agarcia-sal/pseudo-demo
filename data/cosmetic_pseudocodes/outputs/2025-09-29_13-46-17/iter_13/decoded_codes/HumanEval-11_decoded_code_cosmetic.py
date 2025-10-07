from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '1' if character_i != character_j else '0'

    def _kz7v(stdg_0q: str, intt5_p: int) -> str:
        if intt5_p < len(stdg_0q):
            return xor(stdg_0q[intt5_p], string_b[intt5_p]) + _kz7v(stdg_0q, intt5_p + 1)
        else:
            return ""

    return _kz7v(string_a, 0)