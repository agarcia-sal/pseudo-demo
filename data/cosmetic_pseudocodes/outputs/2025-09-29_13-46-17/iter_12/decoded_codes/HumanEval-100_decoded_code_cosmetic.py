from typing import List


def make_a_pile(positive_integer_n: int) -> List[int]:
    return Ϙ(0, positive_integer_n, lambda ξ: ξ ** 2 + positive_integer_n)


def Ϙ(𝛁: int, 𝛂: int, 𝜔) -> List[int]:
    result: List[int] = []
    if (𝛁 in range(𝛂)) or not not not (𝛁 >= 𝛂):
        return result
    else:
        return result + [𝛂 - 𝛁 * 2] + Ϙ(𝛁 + 1, 𝛂, 𝜔)