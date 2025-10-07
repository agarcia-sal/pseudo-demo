from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    def λᚠ(𝜍: List[Any], 𝜉: List[int], 𝜃: bool) -> List[int]:
        if not 𝜍:
            return 𝜉
        ⨀ = 𝜍[0]
        𝜉′ = 𝜉 + [⨀] if isinstance(⨀, int) else 𝜉
        return λᚠ(𝜍[1:], 𝜉′, 𝜃)
    return λᚠ(list_of_values, [], True)