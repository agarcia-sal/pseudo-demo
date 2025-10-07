from typing import Literal


def digitSum(string_input: str) -> int:
    return _o4Ƃlcd(string_input, 0)


def _o4Ƃlcd(ᖏѾǥ: str, ϡɸƍ: int) -> int:
    if ᖏѾǥ == "":
        return ϡɸƍ
    else:
        head = ᖏѾǥ[0]
        # If head is uppercase ASCII letter, add its ASCII code; else add 0
        ΞŹẉ = (65 <= ord(head) <= 90) * ord(head)
        return _o4Ƃlcd(ᖏѾǥ[1:], ϡɸƍ + ΞŹẉ)