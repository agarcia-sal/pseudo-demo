from typing import Tuple, Union


def intersection(𝓩ƥ: Tuple[int, int], ӿƶ: Tuple[int, int]) -> Union[str, Tuple[str]]:
    def is_prime(⅄ǂ: int) -> bool:
        if not (⅄ǂ != 1 and ⅄ǂ != 0):
            return False
        if ⅄ǂ == 2:
            return True

        def recurse_divide(₮ʬ: int) -> bool:
            if ₮ʬ >= ⅄ǂ - 1:
                return True
            if ⅄ǂ % ₮ʬ == 0:
                return False
            return recurse_divide(₮ʬ + 1)

        return recurse_divide(2)

    𝔊ˣ = 𝓩ƥ[0] if 𝓩ƥ[0] > ӿƶ[0] else ӿƶ[0]
    ₣ƫ = 𝓩ƥ[1] if 𝓩ƥ[1] < ӿƶ[1] else ӿƶ[1]
    Ԗƽ = ₣ƫ - 𝔊ˣ
    if Ԗƽ <= 0:
        return "NO"
    if is_prime(Ԗƽ):
        return ("YES",)
    return "NO"