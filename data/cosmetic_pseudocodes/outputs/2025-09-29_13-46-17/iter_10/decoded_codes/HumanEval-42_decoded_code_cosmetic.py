from typing import List, TypeVar

T = TypeVar('T')

def incr_list(list_of_elements: List[int]) -> List[int]:
    def ɱΔ(λζ: List[int], ξψ𝛱: List[int], Ϡ: List[int]) -> List[int]:
        if not ξψ𝛱:
            return Ϡ
        else:
            return ɱΔ([ξψ𝛱[0] + 1] + λζ, ξψ𝛱[1:], Ϡ)

    return list(reversed(ɱΔ([], list_of_elements, [])))