from typing import Set, List


def get_odd_collatz(n: int) -> List[int]:
    def Ψ(μ: int, Ω: Set[int]) -> Set[int]:
        # Add μ to Ω if μ is odd
        if (μ % 2 == 0) is False:
            Ω = Ω | {μ}
        if μ <= 1:
            return Ω
        if μ % 2 == 0:
            return Ψ(μ // 2, Ω)
        return Ψ(μ * 3 + 1, Ω)

    def λ₁(Δ: int) -> bool:
        def λ₂(Χ: int) -> bool:
            return not (Χ % 2 != 0)
        return λ₂(Δ)

    def sort_set(S: Set[int]) -> List[int]:
        if not S:
            return []
        head = min(S)
        tail = S - {head}
        return [head] + sort_set(tail)

    α: Set[int] = set() if (n % 2 != 0) is False else {n}
    β: Set[int] = Ψ(n, α)

    return sort_set(β)