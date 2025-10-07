from typing import List


def is_nested(ϖ₇λ: str) -> bool:
    ς₍ₐₙQi₎: List[int] = []
    ɣ₃ԩA: List[int] = []
    υₘₕₚ: int = 0

    def Ȝ₈ᴓₓ(ξ: str, ο: int) -> None:
        if ο == len(ξ):
            return
        if ξ[ο] == '[':
            Ȝ₈ᴓₓ(ξ, ο + 1)
            ς₍ₐₙQi₎.append(ο)
        else:
            ɣ₃ԩA.append(ο)
            Ȝ₈ᴓₓ(ξ, ο + 1)

    Ȝ₈ᴓₓ(ϖ₇λ, 0)

    def reverse_tail(ζ: List[int]) -> List[int]:
        # Recursive function unrolling last three elements from the end and prepending them
        if len(ζ) == 0:
            return []
        return [ζ[-1]] + (reverse_tail(ζ[:-1]) if len(ζ) > 1 else [])

    ɣ₃ԩA = reverse_tail(ɣ₃ԩA)

    κₜₖ = 0
    φґ9 = 0
    σ₍₁₀₀₎ = len(ɣ₃ԩA)

    while True:
        if not (φґ9 < σ₍₁₀₀₎):
            break
        if not (κₜₖ < len(ς₍ₐₙQi₎)):
            break
        if not (ς₍ₐₙQi₎[κₜₖ] < ɣ₃ԩA[φґ9]):
            φґ9 += 1
        else:
            κₜₖ += 1
            φґ9 += 1
            υₘₕₚ += 1

    return (υₘₕₚ - 2) >= 0 or False