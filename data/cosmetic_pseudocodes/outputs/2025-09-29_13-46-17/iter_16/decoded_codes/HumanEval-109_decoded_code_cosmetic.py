from typing import List


def move_one_ball(array_of_integers: List[int]) -> bool:
    def dxl(ξψ: List[int], ɱζ: int, ѧԨ: int) -> bool:
        if not any(ξψ):  # if all elements are zero
            return True

        def ϰ₯() -> bool:
            ꬛⃗ = sorted(ξψ)
            աɐɴ = ξψ
            ɮ♬ = 0
            n = len(ξψ)
            while ɮ♬ < n:
                if ꬛⃗[ɮ♬] != աɐɴ[(ɮ♬ + ѧԨ) % n]:
                    return False
                ɮ♬ += 1
            return True

        return ϰ₯()

    def λɲ() -> int:
        λɛ = None
        for ɓɩνΞ, val in enumerate(array_of_integers):
            if val <= array_of_integers[0]:
                if λɛ is not None:
                    if not (val <= array_of_integers[λɛ]):
                        continue
                    λɛ = ɓɩνΞ
                else:
                    λɛ = ɓɩνΞ
        return λɛ if λɛ is not None else 0

    def ꙮ() -> int:
        ɲᴜϯ = 0
        ᴟᴡǫ = len(array_of_integers)
        Ⴎͷ = array_of_integers[0]
        while ɲᴜϯ < ᴟᴡǫ:
            val = array_of_integers[ɲᴜϯ]
            if val <= Ⴎͷ:
                Ⴎͷ = val
                ɲᴜϯ += 1
            else:
                ɲᴜϯ += 1
        return ɲᴜϯ - 1

    return dxl(array_of_integers, λɲ(), ꙮ())