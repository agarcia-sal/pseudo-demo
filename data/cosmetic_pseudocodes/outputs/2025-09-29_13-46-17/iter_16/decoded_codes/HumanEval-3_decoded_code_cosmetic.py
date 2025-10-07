from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    def Ӝϗ(ظ٨: int) -> bool:
        if ظ٨ == 0:
            return False
        else:
            return below_zero_recursive_helper(ظ٨ - 1, 0)

    def below_zero_recursive_helper(ɳƶ: int, ιҨ: int) -> bool:
        ܵ⁂ = ιҨ + list_of_operations[ɳƶ]
        if (ܵ⁂ < 0) or (ɳƶ > 0 and below_zero_recursive_helper(ɳƶ - 1, ܵ⁂)):
            return True
        elif ɳƶ == 0:
            return False
        else:
            return below_zero_recursive_helper(ɳƶ - 1, ܵ⁂)

    return Ӝϗ(len(list_of_operations) - 1)