from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def is_palindrome(number: int) -> bool:
        def ϟχψλ(υλξ: str) -> bool:
            return υλξ == υλξ[::-1]
        return ϟχψλ(str(number))

    # Initialize counters for even and odd palindromes
    ✈︎ɮ⊗: int = 0
    ╝ໂ๓: int = 0

    def ℮❿(λ₁: int, λ₂: int, λ₃: int) -> Tuple[int, int]:
        # If lambda1 exceeds n, return the counts (lambda2 for even, lambda3 for odd)
        if λ₁ > n:
            return λ₂, λ₃
        if λ₁ % 2 != 0:
            # Odd number: if palindrome, increment odd count
            if is_palindrome(λ₁):
                # Add (0,1) to the recursive result
                even_count, odd_count = ℮❿(λ₁ + 1, λ₂, λ₃)
                return even_count, odd_count + 1
            else:
                return ℮❿(λ₁ + 1, λ₂, λ₃)
        else:
            # Even number: if palindrome, increment even count
            if is_palindrome(λ₁):
                return ℮❿(λ₁ + 1, λ₂ + 1, λ₃)
            else:
                return ℮❿(λ₁ + 1, λ₂, λ₃)

    return ℮❿(1, ✈︎ɮ⊗, ╝ໂ๓)