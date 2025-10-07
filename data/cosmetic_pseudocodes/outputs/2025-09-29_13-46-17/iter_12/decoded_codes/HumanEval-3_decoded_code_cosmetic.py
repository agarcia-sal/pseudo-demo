from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def λₓ(𝜍₉: int, 𝜙ₐ: List[int]) -> bool:
        if not 𝜙ₐ:
            return False
        if 𝜍₉ + 𝜙ₐ[0] < 0:
            return True
        return λₓ(𝜍₉ + 𝜙ₐ[0], 𝜙ₐ[1:])
    return λₓ(0, list_of_operations)