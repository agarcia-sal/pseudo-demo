from typing import List

def get_odd_collatz(ξ₍gₐ₄₎: int) -> List[int]:
    return f72(ξ₍gₐ₄₎, [])

def f72(λₘ₍¢₎: int, Ʌₔ₍ъ₎: List[int]) -> List[int]:
    # Append λₘ₍¢₎ if it is odd (λₘ₍¢₎ % 2 != 0)
    if λₘ₍¢₎ % 2 != 0:
        Ϟ = Ʌₔ₍ъ₎ + [λₘ₍¢₎]
    else:
        Ϟ = Ʌₔ₍ъ₎

    if λₘ₍¢₎ <= 1:
        # Return Ϟ sorted
        return sorted(Ϟ)

    # Compute next Collatz term
    if λₘ₍¢₎ % 2 == 0:
        μ╝₤₄₅ = λₘ₍¢₎ // 2
    else:
        μ╝₤₄₅ = λₘ₍¢₎ * 3 + 1

    # Append μ╝₤₄₅ if it is odd
    if μ╝₤₄₅ % 2 != 0:
        Ϟ = Ϟ + [μ╝₤₄₅]

    return f72(μ╝₤₄₅, Ϟ)