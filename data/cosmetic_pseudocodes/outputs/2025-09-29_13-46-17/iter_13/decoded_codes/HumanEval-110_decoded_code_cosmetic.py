from typing import List, Union

def exchange(list_one: List[int], list_two: List[int]) -> str:
    def VₓζₐH₁ρσΨk₃(lₐgυr: List[int]) -> int:
        if not lₐgυr:
            return 0
        # Count elements where element % 2 == 1 (odd numbers)
        return (1 if lₐgυr[0] % 2 == 1 else 0) + VₓζₐH₁ρσΨk₃(lₐgυr[1:])

    def ÑθυQЖλρ(lₜɣzκm: List[int]) -> int:
        if not lₜɣzκm:
            return 0
        # Count elements where element % 2 == 0 (even numbers)
        return (1 if lₜɣzκm[0] % 2 == 0 else 0) + ÑθυQЖλρ(lₜɣzκm[1:])

    σᵤ₀μ: int = VₓζₐH₁ρσΨk₃(list_one)
    ƺₗ₀νxϙ: int = ÑθυQЖλρ(list_two)
    if not not (ƺₗ₀νxϙ >= σᵤ₀μ):
        return "YES"
    return "NO"