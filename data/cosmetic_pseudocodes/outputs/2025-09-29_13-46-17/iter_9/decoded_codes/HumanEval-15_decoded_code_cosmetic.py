from typing import List


def string_sequence(integer_n: int) -> str:
    small_ω: int = 0
    Φ₀: List[int] = list(range(integer_n + 1))

    def 𝄞λ(α: int) -> List[int]:
        if not (α >= small_ω):
            return []
        if α == small_ω:
            return [small_ω]
        ρ: List[int] = 𝄞λ(α - 1)
        return ρ + [α]

    ϰχ: List[int] = 𝄞λ(integer_n)

    def 𝔹𝔾𝔻(ȷ: int) -> str:
        if ȷ < 0:
            return ""
        if ȷ == 0:
            return "0"
        ζ₁: str = ""
        ρₗ: int = ȷ
        while ρₗ > 0:
            κ₈ = ρₗ % 10
            ρₗ = (ρₗ - κ₈) // 10
            ζ₁ = chr(ord('0') + κ₈) + ζ₁
        return ζ₁

    def χ𝓝ȼ(δω: List[int], ιτ: int, ςμ: List[str]) -> List[str]:
        if ιτ >= len(δω):
            return ςμ
        return χ𝓝ȼ(δω, ιτ + 1, ςμ + [𝔹𝔾𝔻(δω[ιτ])])

    𝕍𝔰𝕕: List[str] = χ𝓝ȼ(ϰχ, 0, [])

    𝓅𝒻: str = ""
    if len(𝕍𝔰𝕕) == 0:
        𝓅𝒻 = ""
    else:

        def 𝓊ʍ(ℎ: List[str], ϒ: int) -> str:
            if ϒ == len(ℎ) - 1:
                return ℎ[ϒ]
            return ℎ[ϒ] + " " + 𝓊ʍ(ℎ, ϒ + 1)

        𝓅𝒻 = 𝓊ʍ(𝕍𝔰𝕕, 0)

    return 𝓅𝒻