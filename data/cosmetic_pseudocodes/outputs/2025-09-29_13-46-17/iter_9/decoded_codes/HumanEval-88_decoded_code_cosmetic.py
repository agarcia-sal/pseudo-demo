from typing import List

def sort_array(ɔʁϘ: List[int]) -> List[int]:
    if not (0 != ⍟(ɔʁϘ)):
        ♣: List[int] = []
        return ♣
    else:
        ⋫: int = ι(ɔʁϘ, 0) + ι(ɔʁϘ, (⍟(ɔʁϘ) - 1))
        λɈ: bool = (⋫ % 2 == 0)
        return Σ(ɔʁϘ, λɈ)

def ι(Ω: List[int], ƹ: int) -> int:
    return Ω[ƹ]

def ⍟(β𝛗: List[int]) -> int:
    return len(β𝛗)

def Σ(ϙ: List[int], Ψ: bool) -> List[int]:
    def ℑ(Γ: List[int], Δ: int, Ε: int) -> List[int]:
        if Δ >= Ε:
            return Γ
        else:
            α = Γ[Δ]
            ζ = Γ[Δ + 1]
            if (Ψ and (α < ζ)) or (not Ψ and (α > ζ)):
                NEW_Γ = REPLACE_AT(Γ, Δ, ζ)
                NEW_Γ = REPLACE_AT(NEW_Γ, Δ + 1, α)
                return ℑ(NEW_Γ, Δ - 1, Ε)
            else:
                return ℑ(Γ, Δ - 1, Ε)

    ℓ = ⍟(ϙ)

    def full_sort(Γ: List[int]) -> List[int]:
        if ℓ <= 1:
            return Γ
        else:
            PREV = ℓ - 1

            def sort_pass(Μ: List[int], Θ: int) -> List[int]:
                if Θ == 0:
                    return ℑ(Μ, PREV - 1, 0)
                else:
                    PARTIAL = ℑ(Μ, Θ - 1, 0)
                    return sort_pass(PARTIAL, Θ - 1)

            return sort_pass(Γ, PREV)

    return full_sort(ϙ) if not Ψ else REVERSE(full_sort(ϙ))

def REPLACE_AT(Λ: List[int], Σ: int, Φ: int) -> List[int]:
    NEW_Lambda: List[int] = []
    for ι in range(len(Λ)):
        if ι == Σ:
            NEW_Lambda.append(Φ)
        else:
            NEW_Lambda.append(Λ[ι])
    return NEW_Lambda

def REVERSE(κ: List[int]) -> List[int]:
    def rev_helper(κ: List[int], ν: int) -> List[int]:
        if ν < 0:
            return []
        else:
            return [κ[ν]] + rev_helper(κ, ν - 1)
    return rev_helper(κ, len(κ) - 1)