from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    def ●λ₃₇ξκ₌(𝛴πϗₐ: List[int]) -> List[int]:
        if not 𝛴πϗₐ:
            return []
        else:
            return [𝛴πϗₐ[0] + 1] + ●λ₃₇ξκ₌(𝛴πϗₐ[1:])
    return ●λ₃₇ξκ₌(list_of_elements)