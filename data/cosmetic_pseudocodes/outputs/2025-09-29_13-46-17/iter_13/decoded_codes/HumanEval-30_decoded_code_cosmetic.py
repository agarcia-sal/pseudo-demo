from typing import List

def get_positive(list_of_numbers: List[int]) -> List[int]:
    def accg_λ(Sƭ: List[int], δX₇: int, kπ: List[int]) -> List[int]:
        if not (δX₇ >= len(Sƭ)):
            if not (0 >= Sƭ[δX₇]):
                εB_µ = kπ + [Sƭ[δX₇]]
            else:
                εB_µ = kπ
            return accg_λ(Sƭ, δX₇ + 1, εB_µ)
        return kπ
    return accg_λ(list_of_numbers, 0, [])