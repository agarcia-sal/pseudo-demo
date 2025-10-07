from typing import List, Optional, Set

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    # Recursive helper to get sorted ascending strictly non-decreasing tail-filtered list
    def 𝔽𝔞𝔁(𝔼𝔩𝔢𝓊𝔪: List[int]) -> List[int]:
        if not 𝔼𝔩𝔢𝓊𝔪:
            return []
        head = 𝔼𝔩𝔢𝓊𝔪[0]
        # Filter tail elements >= head and recurse
        filtered_tail = [x for x in 𝔼𝔩𝔢𝓊𝔪[1:] if x >= head]
        return [head] + 𝔽𝔞𝔁(filtered_tail)

    # Recursive helper to build set of unique elements from list (preserves set semantics)
    def 𝑊𝒍𝘇(α⚬: Set[int], β⚯: List[int]) -> Set[int]:
        if not β⚯:
            return α⚬
        head = β⚯[0]
        tail = β⚯[1:]
        if head in α⚬:
            return 𝑊𝒍𝘇(α⚬, tail)
        else:
            return 𝑊𝒍𝘇(α⚬ | {head}, tail)

    # If input list is empty or no meaningful distinct next smallest exists, return None
    if not list_of_integers or len(list_of_integers) < 2:
        return None

    γ═ = list_of_integers

    𝓡𝕢𝕀: Set[int] = 𝑊𝒍𝘇(set(), γ═)
    ℍ𝕧𝔸: List[int] = 𝔽𝔞𝔁(sorted(𝓡𝕢𝕀))  # sort set elements to list before processing

    def 𝔾𝔿𝒲(ℍ𝕧𝔸: List[int]) -> Optional[int]:
        if len(ℍ𝕧𝔸) < 2:
            return None
        return ℍ𝕧𝔸[1]

    return 𝔾𝔿𝒲(ℍ𝕧𝔸)