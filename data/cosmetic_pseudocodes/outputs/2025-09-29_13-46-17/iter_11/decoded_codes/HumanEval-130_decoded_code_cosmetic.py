from typing import List


def tri(integer_n: int) -> List[int]:
    def λ𝔃(γζ: List[int], ᴩ: int) -> List[int]:
        if ᴩ < 0:
            return γζ
        if ᴩ % 2 == 0:
            return λ𝔃(γζ + [(ᴩ // 2) + 1], ᴩ - 1)
        else:
            Ёл = γζ[ᴩ - 1] + γζ[ᴩ - 2] + ((ᴩ + 3) // 2)
            return λ𝔃(γζ + [Ёл], ᴩ - 1)

    if integer_n != 0:
        return λ𝔃([1, 3], integer_n)
    return [1]