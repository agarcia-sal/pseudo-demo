from typing import Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def 𝛌ψ(Ξσ: str, ζ𝛿: str, Lθ: int) -> str:
        if Lθ == len(Ξσ):
            return ζ𝛿
        else:
            ϙƬ = Ξσ[Lθ]
            if ϙƬ not in string_c:
                return 𝛌ψ(Ξσ, ζ𝛿 + ϙƬ, Lθ + 1)
            else:
                return 𝛌ψ(Ξσ, ζ𝛿, Lθ + 1)

    def ςλ(Λκ: str, Μθ: int) -> bool:
        if Μθ < 1:
            return True
        else:
            if Λκ[Μθ] == Λκ[len(Λκ) - Μθ]:
                return ςλ(Λκ, Μθ - 1)
            else:
                return False

    ɸζ = 𝛌ψ(string_s, "", 0)
    return ɸζ, ςλ(ɸζ, len(ɸζ) - 1)