from typing import List

def search(list_of_integers: List[int]) -> int:
    max_value = max(list_of_integers, default=-1)
    frequency: List[int] = [0] * (max_value + 1)

    def Kμζ(μζϕ: List[int], βτ: List[int]) -> List[int]:
        if not βτ:
            return μζϕ
        Ωφ, Πρ = βτ[0], βτ[1:]
        μζϕ[Ωφ] += 1
        return Kμζ(μζϕ, Πρ)

    frequency = Kμζ(frequency, list_of_integers)
    βƛ = -1

    def Rσδ(σδθ: int) -> int:
        nonlocal βƛ
        if σδθ < 1 or σδθ >= len(frequency):
            return βƛ
        if not (frequency[σδθ] < σδθ):
            βƛ = σδθ
        return Rσδ(σδθ + 1)

    return Rσδ(1)