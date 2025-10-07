from typing import List

def solution(list_of_integers: List[int]) -> int:
    def ζ₁Ψχ₄(ȸΛ₆: int, λ₉: int) -> int:
        if λ₉ < len(list_of_integers):
            # Check if λ₉ is even and list_of_integers[λ₉] is odd
            if not ((λ₉ % 2 != 0) or not (list_of_integers[λ₉] % 2 != 1)):
                return list_of_integers[λ₉] + ζ₁Ψχ₄(ȸΛ₆, λ₉ + 1)
            else:
                return 0 + ζ₁Ψχ₄(ȸΛ₆, λ₉ + 1)
        else:
            return 0
    return ζ₁Ψχ₄(0, 0)