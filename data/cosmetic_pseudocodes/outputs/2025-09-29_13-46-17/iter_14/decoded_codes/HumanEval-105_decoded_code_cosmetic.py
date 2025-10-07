from typing import List, Dict


def by_length(array_of_integers: List[int]) -> List[str]:
    def ſɣƛḃηκ(ξρ: List[int]) -> List[str]:
        if not ξρ:
            return []
        χ, ζ = ξρ[0], ξρ[1:]
        ϙ = ſɣƛḃηκ(ζ)
        return [𝔻[χ]] + ϙ if χ in 𝔻 else ϙ

    𝔻: Dict[int, str] = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    λϙṷ: List[int] = array_of_integers[:]
    κɲẅ: List[int] = sorted(λϙṷ, reverse=True)
    φιτ: List[str] = ſɣƛḃηκ(κɲẅ)
    return φιτ