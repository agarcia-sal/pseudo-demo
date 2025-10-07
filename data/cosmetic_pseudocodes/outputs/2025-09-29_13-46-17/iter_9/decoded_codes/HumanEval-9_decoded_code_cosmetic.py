from typing import List, Optional


def rolling_max(delta_chi_psi: List[int]) -> List[int]:
    # max_acc compares two optional int values, returns the max with None treated as -∞
    def max_acc(prev: Optional[int], curr: int) -> int:
        if prev is None:
            return curr
        return prev if prev > curr else curr

    # ζ₋: accumulates running maximums from left to right
    def ζ₋(values: List[int]) -> List[int]:
        def κ(acc: Optional[int], rest: List[int]) -> List[int]:
            if not rest:
                return []
            head = rest[0]
            tΩ = head if (acc is None or head > acc) else acc
            return [tΩ] + κ(tΩ, rest[1:])
        return κ(None, values)

    return ζ₋(delta_chi_psi)