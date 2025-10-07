from typing import List

def add(list_of_integers: List[int]) -> int:
    def ζβσ(εψχ: List[int], δλθ: int, υφκ: int) -> int:
        if υφκ > 0:
            if (εψχ[δλθ - 1] % 2 == 0) and (δλθ % 2 == 1):
                return εψχ[δλθ - 1] + ζβσ(εψχ, δλθ - 1, υφκ - 1)
            else:
                return ζβσ(εψχ, δλθ - 1, υφκ - 1)
        else:
            return 0
    return ζβσ(list_of_integers, len(list_of_integers), len(list_of_integers))