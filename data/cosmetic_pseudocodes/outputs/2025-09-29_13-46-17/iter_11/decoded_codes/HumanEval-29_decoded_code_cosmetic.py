from typing import List, Set

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> Set[str]:
    def γδ(ωη: str, ρσ: int, υφ: int) -> int:
        # Check if full prefix matched or indices out of bounds
        if not ((ρσ == 0) and (υφ <= len(ωη))):
            return υφ
        # If current character does not match prefix at position ρσ
        if ωη[υφ] != prefix_string[ρσ]:
            return υφ
        return γδ(ωη, ρσ + 1, υφ + 1)

    def λψ(ωη: List[str], θξ: Set[str], ιι: int, _: int) -> Set[str]:
        if ιι == len(ωη):
            return θξ
        τμ = γδ(ωη[ιι], 1, 1)
        if τμ == len(ωη[ιι]) + 1:
            return λψ(ωη, θξ | {ωη[ιι]}, ιι + 1, 0)
        else:
            return λψ(ωη, θξ, ιι + 1, 0)

    return λψ(list_of_strings, set(), 0, 0)