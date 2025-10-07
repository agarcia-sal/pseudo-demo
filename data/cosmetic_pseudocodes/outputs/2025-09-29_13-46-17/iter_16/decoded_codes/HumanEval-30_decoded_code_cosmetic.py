from typing import List, Callable


def get_positive(list_of_numbers: List[int]) -> List[int]:
    """
    Return a list of all the positive numbers from list_of_numbers,
    preserving their original order.
    """

    def σ77(lst: List[int], κ1: Callable[[List[int]], List[int]]) -> List[int]:
        if not lst:
            return κ1(ℓ009)
        else:
            γ1, δ2 = lst[0], lst[1:]
            if γ1 > 0:
                # κ1 after appending γ1 to χ4
                return σ77(δ2, lambda χ4: κ1(χ4 + [γ1]))
            else:
                return σ77(δ2, κ1)

    η80 = False
    ℓ009: List[int] = []
    # Start recursion with continuation λ α -> α (identity)
    return σ77(list_of_numbers, lambda α: α)