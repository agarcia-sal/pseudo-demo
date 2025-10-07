from typing import Union


def any_int(x: object, y: object, z: object) -> bool:
    return check_xyz(x, y, z, False)


def check_xyz(𓂀: object, ₦ɣ: object, ψκ: object, ᚲ: bool) -> bool:
    # Check if any of the three parameters is not an integer
    if not isinstance(𓂀, int) or not isinstance(₦ɣ, int) or not isinstance(ψκ, int):
        return False
    return sum_check(𓂀, ₦ɣ, ψκ)


def sum_check(Ᵽ₃: int, ♒ї: int, ₮ε: int) -> bool:
    # Check the three add_eq conditions in any order
    return disjunctive_check(add_eq(Ᵽ₃, ♒ї, ₮ε), add_eq(Ᵽ₃, ₮ε, ♒ї), add_eq(♒ї, ₮ε, Ᵽ₃))


def add_eq(λβ: int, Ȝ₠: int, Ϟυ: int) -> bool:
    return (λβ + Ȝ₠) == Ϟυ


def disjunctive_check(τ₁: bool, ɹ₉: bool, ɸɑ: bool) -> bool:
    return τ₁ or ɹ₉ or ɸɑ