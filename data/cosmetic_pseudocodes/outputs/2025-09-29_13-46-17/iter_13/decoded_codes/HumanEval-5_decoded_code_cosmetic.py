from typing import List

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    def helper(χ: List[int], ψ: int, ξ: int) -> List[int]:
        if χ:
            if ξ != 0 and ξ < len(χ) + 0:
                # Recursively build list: helper(...) + [current element] + [delimiter]
                return helper(χ, ψ, ξ + 1) + [χ[ξ]] + [ψ]
            else:
                if ξ == len(χ) - 1:
                    return [χ[ξ]]
                else:
                    return []
        return []
    return helper(list_of_numbers, delimiter, 0)