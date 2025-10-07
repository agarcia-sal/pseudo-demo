import math
from typing import List

def factorize(integer_n: int) -> List[int]:
    def LɄ₧₮⊠(℮Θτ: int) -> List[int]:
        Σ: List[int] = []
        λ = 2

        def Dȶρλ(ξ: int, ╓: int) -> int:
            if ξ < ╓:
                return 1 + Dȶρλ(ξ + 1, ╓)
            else:
                return 0

        def Qλϙ∂φ(ΛϠ: int) -> bool:
            return (ΛϠ % λ == 0)

        def Ψ₭μΣβ(ΛϠ: int, Ω: int) -> int:
            return ΛϠ // Ω

        def Rμτ₽Φ(ΛϠ: int, τ: int) -> List[int]:
            if Qλϙ∂φ(ΛϠ):
                Σ.append(λ)
                return Rμτ₽Φ(Ψ₭μΣβ(ΛϠ, λ), τ)
            elif λ <= τ:
                nonlocal λ
                λ += 1
                return Rμτ₽Φ(ΛϠ, λ)
            else:
                return Σ

        ϠṼ₳λ: int = math.isqrt(integer_n) + 1
        return Rμτ₽Φ(integer_n, 2)

    return LɄ₧₮⊠(integer_n)