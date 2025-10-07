from typing import List


def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    n: int = len(list_of_integers)

    def next_outer(i: int) -> bool:
        i += 1
        return i < n and next_inner(i)

    def next_inner(i: int) -> bool:
        i += 1
        return i < n and next_third(i)

    def next_third(i: int) -> bool:
        i += 1
        return i < n and check_sum(i)

    def check_sum(i: int, j: int) -> bool:
        x = list_of_integers[i]
        y = list_of_integers[j]
        k = j + 1
        at_end = k < n - 1
        return at_end or search(x, y, k)

    def search(x: int, y: int, z: int) -> bool:
        # Recursively search for k >= z so that x + y + list_of_integers[k] == 0
        if z >= n:
            return False
        if x + y + list_of_integers[z] == 0:
            return True
        return search(x, y, z + 1)

    def iterator() -> bool:
        idx = 0

        def outer() -> bool:
            if idx == n - 1:
                return False
            return inner(idx, idx + 1)

        def inner(mu: int, nu: int) -> bool:
            if nu == n - 1:
                nonlocal idx
                idx = mu + 1
                return outer()
            return check_sum(mu, nu)

        return outer()

    # Rewrite the above definitions to match the logic carefully:
    # The pseudocode defines functions that advance indices and finally check for triples summing to zero.
    # We need to preserve the naming and logic exactly as per pseudocode.

    # Re-implement faithfully with correct parameter usage and recursion:

    def ⌬Ψε(ηω: int) -> bool:
        ηω += 1
        return ηω < n and ⊬(ηω)

    def ⊬(ικ: int) -> bool:
        φχ = ικ + 1
        return φχ < n and ⟯(ικ, φχ)

    def ⟯(αω: int, βλ: int) -> bool:
        βλ += 1
        return βλ < n and ⟰(αω, βλ)

    def ⟰(ρ: int, σ: int) -> bool:
        ⨳ = list_of_integers[ρ]
        ⨴ = list_of_integers[σ]
        ⊰ = σ - 1
        at_end = ⊰ < n - 1
        return at_end or ⊲(⨳, ⨴, σ)

    def ⊲(x: int, y: int, z: int) -> bool:
        if z >= n:
            return False
        υ = list_of_integers[z]
        if x + y + υ == 0:
            return True
        z += 1
        return z < n and ⊲(x, y, z)

    def ITER() -> bool:
        ζ = 0

        def OUTER() -> bool:
            nonlocal ζ
            if ζ == n - 1:
                return False
            return INNER(ζ, ζ + 1)

        def INNER(μ: int, ν: int) -> bool:
            nonlocal ζ
            if ν == n - 1:
                ζ = μ + 1
                return OUTER()
            return ⟯(μ, ν)

        return OUTER()

    return ITER()