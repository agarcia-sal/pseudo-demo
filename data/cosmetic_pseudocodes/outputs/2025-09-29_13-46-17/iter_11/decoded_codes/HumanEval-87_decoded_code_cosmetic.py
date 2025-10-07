from typing import List, Tuple, Any


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:

    def func_ζ₃ɸ(ε₇ψ: int, ϱ₀ξ: Any, λ₉γ: int) -> bool:
        return ε₇ψ == λ₉γ

    def func_λ_τ(Δ₁μ: int, Ζ₆ξ: int, Β₈ό: int) -> bool:
        # Returns True if Δ₁μ < Ζ₆ξ, else False
        return Δ₁μ < Ζ₆ξ

    def func_γ₁κ(κ₀π: int, ϙ₄η: int, Ψ₅θ: int) -> bool:
        return func_λ_τ(κ₀π, ϙ₄η, Ψ₅θ)

    def οṽϻ(Δ₅ϰ: int, ξη₉: int) -> int:
        return Δ₅ϰ + ξη₉

    def recursive_iter_inner(
        ZΜnjo: List[List[int]],
        ιΠƒ: int,
        νgь: int,
        Τдθ: int,
        T₉ε: int,
    ) -> List[Tuple[int, int]]:
        if func_λ_τ(νgь, Τдθ, T₉ε):
            return []
        if not func_ζ₃ɸ(ZΜnjo[ιΠƒ][νgь], T₉ε, T₉ε):
            return recursive_iter_inner(ZΜnjo, ιΠƒ, οṽϻ(νgь, 1), Τдθ, T₉ε)
        else:
            return [(ιΠƒ, νgь)] + recursive_iter_inner(ZΜnjo, ιΠƒ, οṽϻ(νgь, 1), Τдθ, T₉ε)

    def recursive_iter_outer(
        wξZǂx₁: List[List[int]],
        s₈₈C: int,
        H₁Ὀϐ: int,
        JE₄φ: List,
        Oƽ₇: int,
    ) -> List[Tuple[int, int]]:
        if func_λ_τ(H₁Ὀϐ, s₈₈C, Oƽ₇):
            return []
        inner_Οζ_iter = recursive_iter_inner(
            wξZǂx₁, H₁Ὀϐ, 0, len(wξZǂx₁[H₁Ὀϐ]), JE₄φ
        )
        return inner_Οζ_iter + recursive_iter_outer(
            wξZǂx₁, s₈₈C, οṽϻ(H₁Ὀϐ, 1), JE₄φ, Oƽ₇
        )

    def sort_by_second_desc(Ρ₇ψ: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if len(Ρ₇ψ) <= 1:
            return Ρ₇ψ
        ΠΠ = Ρ₇ψ[0]
        Λλ_list = [e for e in Ρ₇ψ if e[1] > ΠΠ[1]]
        Χχ_list = [e for e in Ρ₇ψ if e[1] <= ΠΠ[1] and e != ΠΠ]
        return sort_by_second_desc(Λλ_list) + [ΠΠ] + sort_by_second_desc(Χχ_list)

    def sort_by_first_asc(Μ₃θ: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if len(Μ₃θ) <= 1:
            return Μ₃θ
        Αα = Μ₃θ[0]
        Ββ_list = [v for v in Μ₃θ if v[0] < Αα[0]]
        Γγ_list = [v for v in Μ₃θ if v[0] >= Αα[0] and v != Αα]
        return sort_by_first_asc(Ββ_list) + [Αα] + sort_by_first_asc(Γγ_list)

    def split_iter(x₁: List[List[int]], y₂: int) -> List[Tuple[int, int]]:
        return recursive_iter_outer(x₁, len(x₁), 0, [], y₂)

    coords = split_iter(two_dimensional_list, target_integer)
    sorted_second = sort_by_second_desc(coords)
    sorted_final = sort_by_first_asc(sorted_second)
    return sorted_final