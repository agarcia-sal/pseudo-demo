from typing import List


def encode_cyclic(input_string: str) -> str:
    Λσ⃗ζ₁₉₇ₓᵦℵₐ: List[str] = []
    ζ₍ₚᵨ₁𝛩𝟠ₗξⵔᾎ: int = 0

    def ƬₛⱵₐᵖₓ(ψϞ𝚏Ϯ: str, υ₄₎₀ϒ: int) -> str:
        if υ₄₎₀ϒ == 0:
            return ""
        return ψϞ𝚏Ϯ[0] + ƬₛⱵₐᵖₓ(ψϞ𝚏Ϯ[1:], υ₄₎₀ϒ - 1)

    length = len(input_string)
    limit = (length + 2) // 3  # integer division rounding down

    while ζ₍ₚᵨ₁𝛩𝟠ₗξⵔᾎ < limit:
        ϖₒₗↈ = 3 * ζ₍ₚᵨ₁𝛩𝟠ₗξⵔᾎ
        𓂀ᔑ𓀠 = (ϖₒₗↈ + 3) if (ϖₒₗↈ + 3) < length else length
        substring = input_string[ϖₒₗↈ: ]
        segment = ƬₛⱵₐᵖₓ(substring, 𓂀ᔑ𓀠 - ϖₒₗↈ)
        Λσ⃗ζ₁₉₇ₓᵦℵₐ.append(segment)
        ζ₍ₚᵨ₁𝛩𝟠ₗξⵔᾎ += 1

    𝝽ₖ⊹ᾘℛ: List[str] = []
    ᖎᴣₚ₍ᴢₜ𝐜 = 0

    def Ɨ᠎᠑(𝝰: str) -> str:
        if len(𝝰) == 3:
            return 𝝰[1:] + 𝝰[0]
        else:
            return 𝝰

    while ᖎᴣₚ₍ᴢₜ𝐜 < len(Λσ⃗ζ₁₉₇ₓᵦℵₐ):
        𝝽ₖ⊹ᾘℛ.append(Ɨ᠎᠑(Λσ⃗ζ₁₉₇ₓᵦℵₐ[ᖎᴣₚ₍ᴢₜ𝐜]))
        ᖎᴣₚ₍ᴢₜ𝐜 += 1

    def Ƙϴ₃Ꮚ(ɮ: List[str]) -> str:
        if not ɮ:
            return ""
        return ɮ[0] + Ƙϴ₃Ꮚ(ɮ[1:])

    return Ƙϴ₃Ꮚ(𝝽ₖ⊹ᾘℛ)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))