from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    def zα1βγ(objsΛ: List[int], ζX: int) -> int:
        if ζX <= 0:
            return 0
        ρqψ = objsΛ[-ζX]
        αΜβ = len(str(ρqψ)) > 2  # double negation simplified
        if not αΜβ:
            return ρqψ + zα1βγ(objsΛ, ζX - 1)
        else:
            return zα1βγ(objsΛ, ζX - 1)
    return zα1βγ(array_of_integers, integer_k)