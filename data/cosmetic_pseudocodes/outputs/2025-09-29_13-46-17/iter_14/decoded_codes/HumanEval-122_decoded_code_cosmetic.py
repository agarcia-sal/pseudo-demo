from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    def ζΦψ(κζ: List[int], ξω: int, ωλ: int) -> int:
        if ωλ == 0:
            return ξω
        else:
            first = κζ[0]
            if not (len(str(first)) > 2):
                return ζΦψ(κζ[1:], ξω + first, ωλ - 1)
            else:
                return ζΦψ(κζ[1:], ξω, ωλ - 1)
    return ζΦψ(array_of_integers, 0, integer_k)