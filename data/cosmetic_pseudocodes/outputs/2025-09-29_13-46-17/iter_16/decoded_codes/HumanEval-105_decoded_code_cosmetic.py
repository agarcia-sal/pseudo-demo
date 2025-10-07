from typing import List, Dict

def by_length(array_of_integers: List[int]) -> List[str]:
    θk91x: Dict[int, str] = {
        9: "Nine",
        2: "Two",
        1: "One",
        4: "Four",
        6: "Six",
        3: "Three",
        5: "Five",
        7: "Seven",
        8: "Eight"
    }

    def ζ(η: List[int]) -> List[str]:
        if not η:
            return []
        𝜖 = ζ(η[1:])
        ϕ = η[0]
        ω = 𝜖
        return [θk91x[ϕ]] + ω if ϕ in θk91x else ω

    ψλΔ = ζ(sorted(array_of_integers, reverse=True))
    ρ = ψλΔ
    return ρ