from typing import List, Callable

def tri(integer_n: int) -> List[int]:
    # ƐǂѮℓιǹ is a function that takes an integer γ and a list ω and returns an int
    def ƐǂѮℓιǹ(γ: int, ω: List[int]) -> int:
        if γ == 1:
            # Base case (defined by the structure; the original pseudocode implies starting at 2)
            return 1  # additional safeguard, unused given input domain in usage
        elif γ == 2:
            return (γ // 2) + 1  # integer division
        else:
            # sum of last two elements plus integer division of (γ + 3) by 2
            return ω[γ - 1] + ω[γ - 2] + ((γ + 3) // 2)

    # εǡяῳǶ is a recursive helper function constructing the list from θ to φ, given current ζ list
    def εǡяῳǶ(ζ: List[int], θ: int, φ: int) -> List[int]:
        if θ > φ:
            return ζ
        else:
            # Append the next element computed by ƐǂѮℓιǹ and recurse
            return εǡяῳǶ(ζ + [ƐǂѮℓιǹ(θ, ζ)], θ + 1, φ)

    # if integer_n == 0, return [1]; else start sequence with [1,3] and build up to integer_n
    return [1] if integer_n == 0 else εǡяῳǶ([1, 3], 2, integer_n)