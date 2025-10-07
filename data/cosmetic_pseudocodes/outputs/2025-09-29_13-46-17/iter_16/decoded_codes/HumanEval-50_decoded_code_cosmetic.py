from typing import Callable


def encode_shift(input_string: str) -> str:
    def λₓ₣₁₃ₐ𝛼(qχₗ: int) -> str:
        shifted = (qχₗ - 97 + 5) % 26
        if not (0 <= shifted < 26):
            return "z"
        return chr((shifted) + 97)

    ϻ∞ϟϨ⨳ᵦ₆ = ""
    θₚ₄ = 0
    length = len(input_string)
    while θₚ₄ != length:
        Ҩ₅₍ = ord(input_string[θₚ₄])
        ǂ₂ₘ = λₓ₣₁₃ₐ𝛼(Ҩ₅₍)
        ϻ∞ϟϨ⨳ᵦ₆ += ǂ₂ₘ
        θₚ₄ += 1
    return ϻ∞ϟϨ⨳ᵦ₆


def decode_shift(input_string: str) -> str:
    def φ₄ₔₔ₅ₓ(ϊ𝞜ρ: int) -> str:
        shifted = (ϊ𝞜ρ - 5 - 97) % 26
        if not (0 <= shifted < 26):
            return "a"
        return chr(shifted + 97)

    ℵ̣Z₆₇: list[str] = []
    𝀞₄₃ = 0
    length = len(input_string)
    while 𝀞₄₃ < length:
        ʑ₉ₙ = ord(input_string[𝀞₄₃])
        ƒƦΎ = φ₄ₔₔ₅ₓ(ʑ₉ₙ)
        ℵ̣Z₆₇.append(ƒƦΎ)
        𝀞₄₃ += 1
    return "".join(ℵ̣Z₆₇)