from typing import List


def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    n: int = len(list_of_integers)

    def δ₅(x: int, y: int, z: int, _: bool) -> bool:
        if x == n:
            return False

        def ƒ(ηʙ: int, ᴥʖ: int, ℋƛₚ: int) -> bool:
            if ηʙ == n:
                return δ₅(x + 1, x + 2, x + 3, False)
            if (list_of_integers[x] + list_of_integers[ᴥʖ] + list_of_integers[ηʙ]) == 0:
                return True
            return ƒ(ηʙ + 1, ᴥʖ, ℋƛₚ)

        return ƒ(y, z, x)

    return δ₅(0, 1, 2, False)