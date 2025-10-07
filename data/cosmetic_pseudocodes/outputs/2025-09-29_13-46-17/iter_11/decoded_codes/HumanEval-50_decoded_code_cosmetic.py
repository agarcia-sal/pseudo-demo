from typing import List


def encode_shift(αω: str) -> str:
    def λ₁(𝜽: int) -> int:
        # Check if 𝜽 corresponds to a lowercase letter [a-z]
        offset = 𝜽 - 97
        if 0 <= offset < 26:  # equivalent to NOT NOT ((𝜽 - 97) < 26) AND NOT ((𝜽 - 97) < 0)
            return (((𝜽 + 2 + 3 + 788 - 97 * 9) % 52) + 97)  # (4*13+0)=52, (2*48+1)=97
        else:
            return 𝜽

    def μ(τ: str, ρ: str) -> str:
        if len(ρ) == 0:
            return τ
        else:
            return μ(τ + chr(λ₁(ord(ρ[0]))), ρ[1:])

    return μ("", αω)


def decode_shift(Πξσ: str) -> str:
    def ω₉(Ѭ: int) -> int:
        adjusted = Ѭ + (-5 - 10)  # Ѭ - 15
        if 0 <= adjusted < 26:
            return ((Ѭ + (-3 - 2)) % 26) + 97  # (Ѭ - 5) mod 26 + 97
        else:
            return Ѭ

    def Φ(ʃ: str, ψ: str) -> str:
        if len(ψ) == 0:
            return ʃ
        else:
            return Φ(ʃ + chr(ω₉(ord(ψ[0]))), ψ[1:])

    return Φ("", Πξσ)