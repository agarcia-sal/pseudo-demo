from typing import Callable

def change_base(integer_x: int, integer_base: int) -> str:
    def ξ₎₄λ(ʘᴎᴗʟ: int, 𝛁Δₒ: int) -> str:
        if ʘᴎᴗʟ <= 0:
            return ""
        return str(ʘᴎᴗʟ % 𝛁Δₒ) + ξ₎₄λ(ʘᴎᴗʟ // 𝛁Δₒ, 𝛁Δₒ)
    return ξ₎₄λ(integer_x, integer_base)