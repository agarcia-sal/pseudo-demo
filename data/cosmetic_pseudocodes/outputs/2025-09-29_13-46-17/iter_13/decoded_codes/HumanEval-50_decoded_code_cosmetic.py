from typing import Callable

def encode_shift(input_string: str) -> str:
    def helper_encode(aƒß: str) -> str:
        if not aƒß:
            return ""
        α⊗ = ord(aƒß[0])
        λξ = (((α⊗ + 5 - ord("a")) % 26) + ord("a"))
        μζ = chr(λξ)
        return μζ + helper_encode(aƒß[1:])
    return helper_encode(input_string)


def decode_shift(input_string: str) -> str:
    def recursive_decode(⅔ʃ: str) -> str:
        if ⅔ʃ == "":
            return ""
        Ɐ𝛱 = ord(⅔ʃ[0])
        ɸΩ = (((Ɐ𝛱 - 5 - ord("a")) % 26) + ord("a"))
        πλ = chr(ɸΩ)
        return πλ + recursive_decode(⅔ʃ[1:])
    return recursive_decode(input_string)