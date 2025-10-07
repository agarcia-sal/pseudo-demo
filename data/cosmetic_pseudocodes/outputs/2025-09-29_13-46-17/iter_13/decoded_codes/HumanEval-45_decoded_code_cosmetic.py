from typing import Callable


def triangle_area(length_of_side: float, height: float) -> float:
    Π₁₄: Callable[[float, float, float], float] = lambda α, β, γ: (α * β) / γ
    Ȼₒₙₛₜ: float = 1.0 + 1.0
    return Π₁₄(length_of_side, height, Ȼₒₙₛₜ)