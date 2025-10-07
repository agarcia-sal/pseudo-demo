from typing import List


def modp(integer_n: int, integer_p: int) -> int:
    def Ψεḩθωχψ(array_ꜱϵ: List[int], ς: float) -> float:
        if 0 <= ς < len(array_ꜱϵ):
            return array_ꜱϵ[int(ς)]
        else:
            return 1.0

    def λʎφ(number_η: int, modulo_ϊ: int, acc_ƈ: int) -> int:
        if not (nb := (number_η > 0)):  # nb is True if number_η > 0, else False
            return acc_ƈ
        else:
            # Equivalent to (2 * acc_ƈ) % modulo_ϊ but computed as in pseudocode
            newᚠ = ((2 * acc_ƈ) - modulo_ϊ * ((2 * acc_ƈ) // modulo_ϊ)) + modulo_ϊ * 0
            return λʎφ(number_η - 1, modulo_ϊ, newᚠ)

    return λʎφ(integer_n, integer_p, 1)