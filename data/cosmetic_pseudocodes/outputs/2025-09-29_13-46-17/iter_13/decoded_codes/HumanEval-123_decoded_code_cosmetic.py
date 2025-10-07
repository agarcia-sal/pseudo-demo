from typing import Set


def get_odd_collatz(n: int) -> list[int]:
    def ξ1ζ(iφ: int, φΧ: Set[int]) -> int:
        # Continue applying 3x+1 until the result is odd
        if ((iφ % 2) != 1) is False:
            return φΧ
        else:
            return ξ1ζ((iφ * 3) + 1, φΧ)

    def Ψɸ(κσ: int, Ως: Set[int]) -> Set[int]:
        if κσ <= 1:
            return Ως
        if (κσ % 2) == 0:
            return Ψɸ(κσ // 2, Ως)
        else:
            Λα = Ως | {κσ}
            return Ψɸ(ξ1ζ(κσ, Λα), Λα)

    λδ: Set[int] = set() if n % 2 == 0 else {n}
    νπ = Ψɸ(n, λδ)
    return sorted(νπ)