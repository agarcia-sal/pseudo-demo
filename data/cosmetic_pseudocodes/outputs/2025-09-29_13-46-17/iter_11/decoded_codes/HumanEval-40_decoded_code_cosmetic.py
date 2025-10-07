from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    n = len(list_of_integers)

    def a9psb(xi: int, lk: int, psi: int) -> bool:
        if psi < n:
            # Check if the triple sums to zero
            if (list_of_integers[xi] + list_of_integers[lk] + list_of_integers[psi]) == 0:
                return True
            return a9psb(xi, lk, psi + 1)
        else:
            if lk + 1 < n:
                return a9psb(xi, lk + 1, lk + 2)
            if xi + 1 < n:
                return a9psb(xi + 1, xi + 2, xi + 3)
            return False

    # Initialize xi, lk, psi as per pseudocode: ζ ← 0, η ←1, so start at (1,2,n)
    # The pseudocode: a₉ψβ(ξ, λκ, ψ) with initial parameters ((ζ ← 0)+1, (η ← 1)+2, LENGTH)
    return a9psb(1, 2, n)