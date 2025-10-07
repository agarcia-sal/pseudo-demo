from typing import List, Union

def sort_array(αβγΔ: List[Union[int, float]]) -> List[Union[int, float]]:
    # Unsupported inner lambda from pseudocode, defined but unused to match structure
    λξτϕ = lambda: (0, 1)

    if not (len(αβγΔ) == 0):
        ϙς = (lambda ϕψτ: ϕψτ[0] + ϕψτ[len(ϕψτ) - 1])(αβγΔ)
        ϙςχ = (ϙς % 2 == 0)
        return (lambda θφξ: sorted(θφξ, reverse=ϙςχ))(αβγΔ)
    else:
        return []