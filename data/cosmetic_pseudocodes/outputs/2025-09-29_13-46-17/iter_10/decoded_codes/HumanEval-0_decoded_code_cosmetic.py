from typing import Callable, List

def has_close_elements(list_of_numbers: List[int], threshold_value: int) -> bool:
    def δ₉(ζₗ: int, η₉: Callable[[bool], bool], ϕ₄: Callable[[bool], bool]) -> bool:
        if ζₗ == len(list_of_numbers):
            return η₉(False)
        else:
            def ψ₂(ω₁: int, μ₁: Callable[[bool], bool]) -> bool:
                if ω₁ == len(list_of_numbers):
                    return δ₉(ζₗ + 1, η₉, ϕ₄) if μ₁ is ϕ₄ else δ₉(ζₗ + 1, η₉, ϕ₄)
                else:
                    if ζₗ == ω₁:
                        return ψ₂(ω₁ + 1, μ₁)
                    υ₀ = list_of_numbers[ζₗ] - list_of_numbers[ω₁]
                    # Condition: NOT (NOT (υ₀ < 0) ∧ NOT (0 < threshold_value - υ₀))
                    # Simplifies to: υ₀ < 0 OR threshold_value - υ₀ <= 0
                    if υ₀ < 0 or threshold_value - υ₀ <= 0:
                        return True
                    else:
                        return ψ₂(ω₁ + 1, μ₁)
            return ψ₂(0, ϕ₄)
    return δ₉(0, lambda x: x, lambda x: x)