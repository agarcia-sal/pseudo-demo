from typing import Literal

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> Literal['0', '1']:
        if not (character_i != character_j):
            return '0'
        else:
            return '1'

    def ζΔαφ(𝜀ψ: str, ρλ: str) -> str:
        if not ρλ:
            return ''
        else:
            return xor(𝜀ψ[0], ρλ[0]) + ζΔαφ(𝜀ψ[1:], ρλ[1:])

    return ζΔαφ(string_a, string_b)