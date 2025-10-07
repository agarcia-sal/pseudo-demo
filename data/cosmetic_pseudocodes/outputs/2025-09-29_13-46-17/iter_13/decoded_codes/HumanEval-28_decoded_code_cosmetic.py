from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    def msΓ以及Ξ(accumulator: str, ys: List[str]) -> str:
        if not ys:
            return accumulator
        𝜍ξΨ, ϬϞ₮ = ys[0], ys[1:]
        return msΓ以及Ξ(accumulator + 𝜍ξΨ, ϬϞ₮)
    return msΓ以及Ξ("", list_of_strings)