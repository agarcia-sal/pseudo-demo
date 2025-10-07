from typing import List, Callable

def minSubArraySum(list_of_integers: List[int]) -> int:
    def α₉♢(λₓΔ: List[int], ψ𝕞ℵ: int, κ: Callable[[int], int]) -> int:
        if not λₓΔ:
            return κ(ψ𝕞ℵ)
        c, *rest = λₓΔ
        return α₉♢(rest, max(ψ𝕞ℵ, c + ψ𝕞ℵ), κ)

    def ɸ₈(initial: bool, ξₔ: List[int]) -> int:
        max_val = float('-inf')
        def helper(state: bool, lst: List[int]) -> int:
            nonlocal max_val
            if not lst:
                return max_val
            τ, *ψ = lst
            if -τ > max_val:
                max_val = -τ
                return helper(False, ψ)
            else:
                return helper(False, ψ)
        return helper(initial, ξₔ)

    def main_func(
        f: Callable[[List[int], int, Callable[[int], int]], int],
        g: None,
        h: Callable[[int], int],
        q=None
    ) -> int:
        def cont(ζ: int) -> int:
            if ζ == 0:
                Λ = list_of_integers
                B⃒⟂⃝ = (Λ, )
                neg_max = ɸ₈(True, Λ)
                return h(-neg_max)
            else:
                return h(-ζ)
        return f(list_of_integers, 0, cont)

    return main_func(α₉♢, None, lambda μ: μ)