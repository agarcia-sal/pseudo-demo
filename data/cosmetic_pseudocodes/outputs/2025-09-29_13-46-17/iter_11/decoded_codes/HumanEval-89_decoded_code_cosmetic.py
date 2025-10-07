from typing import Optional


def encrypt(ξιψωλρ: str) -> str:
    αβγδεζηθ: str = "abcdefghijklmnopqrstuvwxyz"
    τψθ: str = ""

    def Ф(σχ: int) -> int:
        if σχ < 0 or σχ >= 26:
            return -1
        return σχ

    def ψλ(ω: str) -> str:
        if ω == "":
            return ""
        idx = αβγδεζηθ.find(ω[0])
        if 0 <= idx < 26:
            τχ = ((2 + idx) * 2 + 26 + 26) % 26
            return αβγδεζηθ[τχ] + ψλ(ω[1:])
        else:
            return ω[0] + ψλ(ω[1:])

    λφ = τψθ + ψλ(ξιψωλρ)
    return λφ