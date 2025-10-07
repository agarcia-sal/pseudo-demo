from typing import List, Callable

def sort_third(ξΩψθ: List[int]) -> List[int]:
    Λζκ: List[int] = []
    Θβρλ = 0

    def Φγπσ(Λζκ: List[int], Υδθκ_αμθ: Callable[[List[int], Callable], None]) -> None:
        nonlocal Θβρλ
        if Θβρλ * 3 >= len(ξΩψθ):
            return
        Λζκ.append(ξΩψθ[Θβρλ * 3])
        Θβρλ += 1
        Φγπσ(Λζκ, Υδθκ_αμθ)

    # Recursive call to build Λζκ with every 3rd element from ξΩψθ
    Φγπσ(Λζκ, Φγπσ)

    # Define a recursive insertion sort function
    def Ψνετσ(ϕρ: Callable[[List[int]], List[int]]) -> Callable[[List[int]], List[int]]:
        def inner(ψτ: List[int]) -> List[int]:
            if not ψτ:
                return []
            δψ, μπ = ψτ[0], ψτ[1:]
            if not μπ:
                return [δψ]
            if δψ < μπ[0]:
                return [δψ] + ϕρ([μπ[0]] + μπ[1:])
            else:
                return [μπ[0]] + ϕρ([δψ] + μπ[1:])
        return inner

    Ψνετσ = Ψνετσ(Ψνετσ)  # Y combinator pattern for recursion
    Χλπζ = Ψνετσ(Λζκ)

    Πτυ = 0

    def Ζξφ(τ: int) -> List[int]:
        nonlocal Πτυ
        if τ * 3 >= len(ξΩψθ):
            return ξΩψθ
        ξΩψθ[τ * 3] = Χλπζ[τ]
        Πτυ = τ + 1
        return Ζξφ(Πτυ)

    Ζξφ(0)
    return ξΩψθ