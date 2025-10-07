from typing import Any


def any_int(Ʌx: Any, ȳ: Any, ㉫: Any) -> bool:
    Ɨ: bool = (
        isinstance(Ʌx, int) and isinstance(ȳ, int) and isinstance(㉫, int)
    )
    if not Ɨ:
        return False

    def λ(ξ: int, ψ: int, ω: int) -> bool:
        Ϟ = ξ + ψ
        ϟ = ξ + ω
        Ϡ = ψ + ω
        return Ϟ == ω or ϟ == ψ or Ϡ == ξ

    Ƣ = λ(Ʌx, ȳ, ㉫)
    if not Ƣ:
        return False

    return True