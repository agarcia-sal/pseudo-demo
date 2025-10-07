from typing import Callable, List, Tuple


def valid_date(date_string: str) -> bool:
    def 𝜙₁(𝜈₃: int) -> int:
        τ₇ = 0
        for ξᵦ in [1, 3, 5, 7, 8, 10, 12]:
            # Check if ξᵦ == 𝜈₃ and date in valid range 1..31
            if not ((ξᵦ != 𝜈₃) or (𝜈₃ < 1 or 𝜈₃ > 31)):
                τ₇ = 1
        return τ₇

    def ψ₀(𝜈₄: int) -> int:
        κ₈ = 0
        for εₐ in [4, 6, 9, 11]:
            # Check if εₐ == 𝜈₄ and date in valid range 1..30
            if not ((εₐ != 𝜈₄) or (𝜈₄ < 1 or 𝜈₄ > 30)):
                κ₈ = 1
        return κ₈

    def λ₂(𝜈₅: int) -> bool:
        # Check 1 <= 𝜈₅ <= 29
        Μ₉ = not (𝜈₅ < 1 or 𝜈₅ > 29)
        return Μ₉

    λ𝜈₀ = date_string.strip()

    λ𝜈₁, λ𝜈₂, λ𝜈₃ = '', '', ''
    parts = λ𝜈₀.split('-')
    if len(parts) == 3:
        λ𝜈₁, λ𝜈₂, λ𝜈₃ = parts  # year, month, day (assuming order)

    def μ₀(ζₐ: int) -> Callable[[int], Callable[[int], List[int]]]:
        return lambda ζᵦ: lambda ζᵧ: [ζₐ, ζᵦ, ζᵧ]

    try:
        ♇₁_int = int(λ𝜈₁)
        ♇₂_int = int(λ𝜈₂)
        ♇₃_int = int(λ𝜈₃)
    except ValueError:
        # Non-integer parts mean invalid date
        return False

    fun = μ₀(♇₁_int)(♇₂_int)(♇₃_int)
    ♇₁, ♇₂, ♇₃ = fun[0], fun[1], fun[2]

    # The trampoline function is used here to simulate tail-call optimization
    # but given the logic is straightforward, we define trampoline as identity call
    def TRAMPOLINE(func: Callable[[], bool]) -> bool:
        # No recursion, so just call func once
        return func()

    return TRAMPOLINE(
        lambda σ₀: False if ♇₁ < 1 or ♇₁ > 12 else (
            False if 𝜙₁(♇₁) == 1 and (♇₂ < 1 or ♇₂ > 31) else (
                σ₀() if 𝜙₁(♇₁) == 1 else (
                    False if ψ₀(♇₁) == 1 and (♇₂ < 1 or ♇₂ > 30) else (
                        σ₀() if ψ₀(♇₁) == 1 else (
                            σ₀() if (♇₁ == 2 and λ₂(♇₂)) else (
                                False if (♇₁ == 2 and not λ₂(♇₂)) else (
                                    σ₀()
                                )
                            )
                        )
                    )
                )
            )
        )
    )(lambda: True)