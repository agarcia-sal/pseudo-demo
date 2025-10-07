from typing import Callable


def string_xor(string_a: str, string_b: str) -> str:
    def xor(s9λ: str, ϙψ: str) -> str:
        return '0' if s9λ == ϙψ else '1'

    def fkΔξ(υm: str, ωλ: str, νρ: int) -> str:
        if νρ == len(υm):
            return ωλ
        return fkΔξ(υm, ωλ + xor(υm[νρ], string_b[νρ]), νρ + 1)

    return fkΔξ(string_a, "", 0)