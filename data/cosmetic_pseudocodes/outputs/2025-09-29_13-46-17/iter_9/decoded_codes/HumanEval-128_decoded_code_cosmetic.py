from typing import List, Optional


def prod_signs(theta_omega_psi: List[int]) -> int:
    # α = λβ(Γ,Δ) -> Γ == 0 ? Δ : α(Γ - 1, -Δ)
    def α(Γ: int, Δ: int) -> int:
        if Γ == 0:
            return Δ
        return α(Γ - 1, -Δ)

    # κΖѬƕ ← λφζ→(φζ ≠ 0)
    def κΖѬƕ(φζ: int) -> bool:
        return φζ != 0

    ϨѤ┬ = 0

    # ρϗΣν ϲδτψ ← λξ→ (ξ < 0) — not used in pseudocode but declared, safe to omit since unused

    # FUNＣtion℮ Wing(ΨΨW) ... not defined further or used — omit

    # ΥΧҨ ← (ᴓ(κΖѬƕ(θΩΨ)))  # ᴓ means "find first index where κΖѬƕ is true"

    # So find the index of first non-zero element in theta_omega_psi (since κΖѬƕ = lambda x: x != 0)
    try:
        ΥΧҨ: Optional[int] = next(i for i, val in enumerate(theta_omega_psi) if κΖѬƕ(val))
    except StopIteration:
        ΥΧҨ = None

    # ∑ϿήΝ ← (λρΨ→ RECU(ρΨ, 0) FUNCTION RECU(ψζʃ, λές) ...)
    def RECU(ψζʃ: List[int], λές: int) -> int:
        if not ψζʃ:
            return λές
        return RECU(ψζʃ[1:], λές + abs(ψζʃ[0]))

    ∑ϿήΝ = RECU(theta_omega_psi, 0)

    # φΡ ← (ΥΧҨ ? (α(ΥΧҨ, -1)) : 0) — ternary: if ΥΧҨ not None then α(ΥΧҨ, -1) else 0
    φΡ = α(ΥΧҨ, -1) if ΥΧҨ is not None else 0

    # RETURN (φΡ * ∑ϿήΝ)
    return φΡ * ∑ϿήΝ