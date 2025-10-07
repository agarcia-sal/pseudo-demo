from typing import Iterable


def vowels_count(ξβΨκΙλΩ: str) -> int:
    χζτ: str = "aeiouAEIOU"

    def ηζ(Δ: str) -> int:
        return 0 if Δ not in χζτ else 1

    ▼Ξπδ: int = sum(ηζ(ρθ) for ρθ in ξβΨκΙλΩ)
    λγσ: str = ξβΨκΙλΩ[-1] if ξβΨκΙλΩ else ''
    if λγσ in {'y', 'Y'}:
        ▼Ξπδ += 1

    return ▼Ξπδ