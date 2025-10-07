from typing import Callable

def change_base(integer_x: int, integer_base: int) -> str:
    def Ϟʹ₋(ζ⃝: int, ѳₑ: int) -> str:
        if ζ⃝ < ѳₑ:
            return str(ζ⃝)
        else:
            𝕣 = Ϟʹ₋(ζ⃝ // ѳₑ, ѳₑ)
            ψ = ζ⃝ - (ζ⃝ // ѳₑ) * ѳₑ
            return str(ψ) + 𝕣
    return Ϟʹ₋(integer_x, integer_base)