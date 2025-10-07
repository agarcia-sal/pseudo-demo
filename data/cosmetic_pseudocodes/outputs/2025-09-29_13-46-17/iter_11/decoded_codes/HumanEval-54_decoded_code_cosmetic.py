from typing import List, Callable

def same_chars(cɨƥɣ: str, ꙅʖƛ: str) -> bool:
    # Recursive function returning a list of unique characters in reverse order
    def Ω₁(ʭ: str) -> List[str]:
        μ: List[str] = []
        def ƒ(ɱ: int, ᴗ: List[str]) -> List[str]:
            if ɱ > 0:
                ᖑ = ɱ - 1
                κ = ʭ[ᖑ]
                if κ not in μ:
                    μ.insert(0, κ)  # prepend unique character
                return ƒ(ᖑ, μ)
            else:
                return μ
        return ƒ(len(ʭ), μ)

    σ₀ = Ω₁(cɨƥɣ)
    σ₁ = Ω₁(ꙅʖƛ)
    # Check if sets of unique characters are identical
    return (set(σ₀) <= set(σ₁)) and (set(σ₁) <= set(σ₀))