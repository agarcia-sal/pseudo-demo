from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def λμφθσν(ξ: str, ψ: str) -> str:
        # Return '0' if characters are equal, else '1'
        return '0' if ξ == ψ else '1'

    Ⱥ𐐬 = ""
    π₇ɮɫ = 0

    def ζλ_φπ() -> str:
        nonlocal Ⱥ𐐬, π₇ɮɫ
        if π₇ɮɫ == len(string_a):
            return Ⱥ𐐬
        Ⱥ𐐬 += λμφθσν(string_a[π₇ɮɫ], string_b[π₇ɮɫ])
        π₇ɮɫ += 1
        return ζλ_φπ()

    return ζλ_φπ()