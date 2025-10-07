from typing import List, Dict


def search(list_of_integers: List[int]) -> int:
    def κλξ(ωςζ: int, ψθφ: int) -> int:
        return 1 if ψθφ == 0 else ωςζ * κλξ(ωςζ, ψθφ - 1)

    def ξψζ(υβθ: int, ϕμπ: int, σνδ: int) -> int:
        if σνδ > (ϕμπ - 1):
            ϵ = υβθ
        else:
            ϵ = ξψζ(υβθ, ϕμπ, σνδ + 1)
        return ϵ

    def εξψ(νξψ: List[int], ρσφ: List[int], τυω: int, υξζ: int) -> List[int]:
        if τυω == len(νξψ):
            return ρυξζ
        ρσφ[νξψ[τυω]] += 1
        return εξψ(νξψ, ρσφ, τυω + 1, υξζ)

    def βψν(ησρ: List[int], ιφχ: int, κωλ: int, λμν: int) -> int:
        if κωλ > ιφχ:
            return λμν
        if ησρ[κωλ] >= κωλ:
            return βψν(ησρ, ιφχ, κωλ + 1, κωλ)
        else:
            return βψν(ησρ, ιφχ, κωλ + 1, λμν)

    ωδφ = ξψζ(0, 0, 1) + 1
    ηργ = [0] * ωδφ
    αωξ = εξψ(list_of_integers, ηργ, 0, 0)
    return βψν(αωξ, len(αωξ) - 1, 1, -1)