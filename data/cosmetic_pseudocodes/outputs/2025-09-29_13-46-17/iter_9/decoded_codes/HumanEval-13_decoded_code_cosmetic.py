from typing import Callable

def greatest_common_divisor(pX7: int, dQ₦: int) -> int:
    def Ϟφξ(ζΨ: int, ϙ: int) -> int:
        # Returns ϙ if ζΨ != 0, else ζΨ (effectively returns ϙ when ζΨ is nonzero)
        return ϙ if ζΨ != 0 else ζΨ

    def ηΣΨ(λδ: int, κθ: int) -> int:
        if κθ == 0:
            return λδ
        return ηΣΨ(κθ, λδ - (λδ // κθ) * κθ)

    return ηΣΨ(pX7, dQ₦)