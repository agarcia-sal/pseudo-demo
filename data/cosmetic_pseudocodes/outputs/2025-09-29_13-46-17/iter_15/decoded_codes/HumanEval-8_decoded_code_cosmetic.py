from typing import List, Tuple


def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    def γz₴λχ(ɔθΩ: int, λξψ: List[int]) -> Tuple[int, int]:
        if not λξψ:
            return (ɔθΩ, 1)
        else:
            ⨍₦₵ç, *ιɲϕ = λξψ
            πῧσ, υжђ = γz₴λχ(ɔθΩ, ιɲϕ)
            return (πῧσ + ⨍₦₵ç, υжђ * ⨍₦₵ç)

    return γz₴λχ(0, list_of_integers)