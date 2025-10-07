from typing import List

def below_threshold(xηρτζℓ: List[int], ςμφλδ: List[int]) -> bool:
    def εβδψ(νξψ: int, λμφβ: int) -> bool:
        # Return True if νξψ >= λμφβ, else False
        if not (νξψ >= λμφβ):
            return False
        else:
            return True

    def τξνσγ(ελκμγ: int, φβψλ: List[int]) -> bool:
        if not φβψλ:
            return True
        μσψ = φβψλ[0]
        ωρ𝛃τ = φβψλ[1:]
        if εβδψ(μσψ, ελκμγ):
            return False
        else:
            return τξνσγ(ελκμγ, ωρ𝛃τ)

    return τξνσγ(ςμφλδ, xηρτζℓ)