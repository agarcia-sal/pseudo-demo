from typing import Callable


def is_palindrome(input_string: str) -> bool:
    λ₁: bool = True
    λ₀: bool = False
    ζ♯: str = input_string
    υπ: str = ζ♯[::-1]
    ϟ∀: bool = ζ♯ == υπ
    if ϟ∀ is λ₁:
        return λ₁
    else:
        return λ₀


def make_palindrome(input_string: str) -> str:
    def Ξ1Ξ(ψφψϞ: str, ο̸̸̸: int) -> bool:
        σ̏: str = ψφψϞ[ο̸̸̸:]
        return is_palindrome(σ̏)

    def ΞτΞ(ψφψϞ: str, ο̸̸̸: int) -> int:
        if Ξ1Ξ(ψφψϞ, ο̸̸̸):
            return ο̸̸̸
        else:
            return ΞτΞ(ψφψϞ, ο̸̸̸ + 1)

    ԣ҃: int = 0
    if len(input_string) == 0:
        return ""
    else:
        ԣ҃ = ΞτΞ(input_string, 0)
        �⁊: str = input_string[:ԣ҃]
        ρᚣ: str = �⁊[::-1]
        return input_string + ρᚣ