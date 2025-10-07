from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    def ⧫λξφψ(ϕξ: int) -> List[int]:
        if ϕξ == 0:
            return []
        else:
            return [list_of_elements[len(list_of_elements) - ϕξ] + 1] + ⧫λξφψ(ϕξ - 1)
    return ⧫λξφψ(len(list_of_elements))