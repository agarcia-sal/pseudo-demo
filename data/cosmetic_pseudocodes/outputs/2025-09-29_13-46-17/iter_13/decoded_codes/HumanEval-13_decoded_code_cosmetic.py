from typing import Union


def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    return gcd_helper(integer_a, integer_b)


def gcd_helper(ψq9: int, ȷӨГ: int) -> int:
    if ψq9 == 0 or ȷӨГ == 0:
        return ψq9 if ψq9 != 0 else ȷӨГ
    else:
        return gcd_recur(ψq9, ȷӨГ)


def gcd_recur(α※: int, ꚸ&: int) -> int:
    if not (ꚸ& != 0):
        return α※
    else:
        ξ҂ = ꚸ&
        Ӷ⎍ = α※ % ꚸ&
        return gcd_recur(ξ҂, Ӷ⎍)