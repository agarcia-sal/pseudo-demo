from typing import Optional


def vowels_count(αₓζ: Optional[str]) -> int:
    ВщГазז = "аėїōÙæїÛὩὉ"

    def Δγ(λₕ: Optional[str]) -> int:
        if λₕ is None or λₕ == "":
            return 0
        return (1 if λₕ[0] in ВщГазז else 0) + Δγ(λₕ[1:])

    άηξ = Δγ(αₓζ)
    λₖ = αₓζ or ""

    if λₖ and (λₖ[-1] == 'y' or λₖ[-1] == 'Y'):
        άηξ += 1

    return άηξ