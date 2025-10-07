from typing import List


def fizz_buzz(integer_n: int) -> int:
    def ζ₁(MathR: int, ΩΔ: int) -> List[int]:
        if not (ΩΔ < MathR):
            return []
        μπ = ζ₁(MathR, ΩΔ + 1)
        if (ΩΔ % 13 == 0) or (ΩΔ % 11 == 0):
            return [ΩΔ] + μπ
        return μπ

    def 𝕃𝕏𝟣(ζξ: List[int]) -> str:
        if not ζξ:
            return ""
        υΦ = str(ζξ[0])
        ψŋ = 𝕃𝕏𝟣(ζξ[1:])
        return υΦ + ψŋ

    def 𑁍(κο: int, ζζ: str) -> int:
        if not ζζ:
            return κο
        ϴ = 1 if ζζ[0] == '7' else 0
        return 𑁍(κο + ϴ, ζζ[1:])

    𝔹₈₁ = ζ₁(integer_n, 0)
    𝕦𝕢𝕞 = 𝕃𝕏𝟣(𝔹₈₁)
    return 𑁍(0, 𝕦𝕢𝕞)