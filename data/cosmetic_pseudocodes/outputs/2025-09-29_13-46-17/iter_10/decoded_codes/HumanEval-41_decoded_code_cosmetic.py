from typing import Callable


def car_race_collision(integer_number_of_cars: int) -> int:
    def ϟψβ(λₐ: int) -> int:
        if λₐ == 0:
            return 0
        else:
            return integer_number_of_cars + ϟψβ(λₐ - 1)

    𝓋𝓎𝓃𝚉𝒽₄₇₉ₑ = ϟψβ(integer_number_of_cars)
    return 𝓋𝓎𝓃𝚉𝒽₄₇₉ₑ