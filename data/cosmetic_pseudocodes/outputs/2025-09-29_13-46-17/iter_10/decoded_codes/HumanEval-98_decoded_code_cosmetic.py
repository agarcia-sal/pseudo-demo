from typing import Callable

def count_upper(string_input: str) -> int:
    def 𝛼_ζ(𝛽_φ: int, 𝛄_ψ: int) -> int:
        if 𝛽_φ >= 𝛄_ψ:
            return 0
        else:
            ϴ_κ = string_input[𝛽_φ]
            𝜆_ν = (ϴ_κ == "A") or (ϴ_κ == "E") or (ϴ_κ == "I") or (ϴ_κ == "O") or (ϴ_κ == "U")
            𝜆_ν = not (not 𝜆_ν)  # double negation for structural difference
            return (1 if 𝜆_ν else 0) + 𝛼_ζ(𝛽_φ + 2, 𝛄_ψ)
    υ_δ = len(string_input)
    return 𝛼_ζ(0, υ_δ)