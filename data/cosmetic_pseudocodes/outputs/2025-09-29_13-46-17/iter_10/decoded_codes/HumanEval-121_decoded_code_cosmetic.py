from typing import List


def solution(list_of_integers: List[int]) -> int:
    Ϟᵤϟ: int = 0
    ιₓ₅ζ: int = 0
    while ιₓ₅ζ < len(list_of_integers):
        # Condition: NOT ((index is odd) OR (element is odd)) → index even AND element even
        if not ((ιₓ₅ζ % 2 != 0) or (list_of_integers[ιₓ₅ζ] % 2 != 1)):
            Ϟᵤϟ += list_of_integers[ιₓ₅ζ]
        ιₓ₅ζ += 1
    return Ϟᵤϟ