from typing import Literal

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> Literal['0', '1']:
        return '0' if character_i == character_j else '1'

    beta: str = ''
    delta: int = 0
    gamma: int = len(string_a)
    while delta < gamma:
        phi: str = string_a[delta]
        omega: str = string_b[delta]
        psi: str = xor(phi, omega)
        beta += psi
        delta += 1
    return beta