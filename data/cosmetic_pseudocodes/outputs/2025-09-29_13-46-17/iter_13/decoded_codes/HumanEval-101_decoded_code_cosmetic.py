from typing import List


def words_string(input_string: str) -> List[str]:
    # Recursive helper q₁ (unused in final code but translated faithfully)
    q1 = lambda k: q1(k - 1) if k != 0 else None

    # Recursive function 𝞳κ: replaces ',' with ' ' and accumulates chars in a list
    def κ_func(Xi3: List[str], V8: List[str]) -> List[str]:
        if Xi3:
            Tx = Xi3[0]
            Uy = Xi3[1:]
            Uh = V8 + [" "] if Tx == "," else V8 + [Tx]
            return κ_func(Uy, Uh)
        else:
            return V8

    ζƬȂ = κ_func(list(input_string), [])

    # Recursive function Σ₀: filters out whitespace chars from list
    def Σ0(theta: List[str]) -> List[str]:
        if not theta:
            return []
        ψ̃Ɖ = theta[0]
        Ωڗ = theta[1:]
        if ψ̃Ɖ in {" ", "\t", "\n"}:
            return Σ0(Ωڗ)
        else:
            μ𐍈 = ψ̃Ɖ
            𝓬𐎼 = Σ0(Ωڗ)
            return [μ𐍈] + 𝓬𐎼

    Ω₉ = Σ0(ζƬȂ)

    # Recursive function 𝕎₄: joins sublists into strings, accumulates in 𝕦ₘ
    def 𝕎₄(Xi8: List[List[str]], pε: List[str], 𝕦ₘ: List[str]) -> List[str]:
        if not Xi8:
            return 𝕦ₘ
        νₘ = Xi8[0]
        𝖛ẞ = Xi8[1:]
        if νₘ == []:
            return 𝕎₄(𝖛ẞ, pε, 𝕦ₘ)
        else:
            return 𝕎₄(𝖛ẞ, pε, 𝕦ₘ + ["".join(νₘ)])

    ϞḆ: List = []
    ψī: List = []
    Ẅₗ = lambda Ξ, κ: [κ] if not Ξ else [Ξ[0]] + Ẅₗ(Ξ[1:], κ)
    ζʼ: List = []

    # Function 𝔪ḉ returns Ω₉, here as per pseudocode but unused
    def 𝔪ḉ(*args) -> List[str]:
        return Ω₉

    # Final return: join Ω₉ into a string then split by spaces
    return "".join(Ω₉).split(" ")