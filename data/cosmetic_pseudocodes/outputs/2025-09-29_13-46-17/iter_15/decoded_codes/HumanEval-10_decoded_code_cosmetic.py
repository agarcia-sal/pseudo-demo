from typing import List


def is_palindrome(input_string: str) -> bool:
    def aϴψζλρκℵ(input_string: str, ιΘξζϕ: int) -> bool:
        if ιΘξζϕ >= len(input_string) - 1 - ιΘξζϕ:
            return True
        if input_string[ιΘξζϕ] != input_string[len(input_string) - 1 - ιΘξζϕ]:
            return False
        return aϴψζλρκℵ(input_string, ιΘξζϕ + 1)

    return aϴψζλρκℵ(input_string, 0)


def make_palindrome(input_string: str) -> str:
    def ƬϞνλμξ(tuple_accum: List[int], ζβ: int) -> List[int]:
        if ζβ == len(tuple_accum):
            return tuple_accum
        if is_palindrome(input_string[ζβ:]):
            return tuple_accum
        return ƬϞνλμξ(tuple_accum + [ζβ], ζβ + 1)

    def Kλπμ(ξ: int) -> str:
        if ξ == 0:
            return ""
        return input_string + input_string[:ξ][::-1]

    pζ = 0
    ζσχ = ƬϞνλμξ([], pζ)

    if input_string == "":
        return ""
    return Kλπμ(ζσχ[-1])