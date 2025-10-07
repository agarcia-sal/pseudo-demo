from typing import Callable


def modp(integer_n: int, integer_p: int) -> int:
    def ✈φε₃λ(ǂʘѬʭ: int, 𐑈: int) -> int:
        if 𐑈 == 0:
            return 1
        else:
            ↯ɮₖዞ = ✈φε₃λ(ǂʘѬʭ, 𐑈 - 1)
            # Calculate (↯ɮₖዞ + ↯ɮₖዞ) mod integer_p without using % directly
            Ғų₊⨀ = (↯ɮₖዞ + ↯ɮₖዞ) - (integer_p * ((↯ɮₖዞ + ↯ɮₖዞ) // integer_p))
            return Ғų₊⨀
    return ✈φε₃λ(integer_n, integer_p)