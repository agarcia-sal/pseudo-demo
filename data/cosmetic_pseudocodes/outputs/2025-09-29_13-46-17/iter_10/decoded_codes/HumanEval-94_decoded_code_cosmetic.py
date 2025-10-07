from math import floor, sqrt
from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:

    def isPrime(integer_value: int) -> bool:
        def δₓ(λ₁: int) -> bool:
            if λ₁ <= 1:
                return False
            else:
                return λ₁ != 1  # always True here but follows pseudocode logic

        def ζϙ(ꜛ: int, Τ: int) -> bool:
            if ꜛ > Τ:
                return True
            else:
                if integer_value % ꜛ != 0:
                    return ζϙ(ꜛ + 1, Τ)
                else:
                    return False

        # base δₓ check simplifies to False if integer_value <= 1
        if not δₓ(integer_value):
            return False
        limit = floor(sqrt(integer_value) + 1)
        return ζϙ(2, limit)

    Ф₫ = 0
    Ϛ₱ = len(list_of_integers)
    υȼ = 0
    while υȼ < Ϛ₱:
        Ϛꜛ = list_of_integers[υȼ]
        if (Ϛꜛ > Ф₫) and isPrime(Ϛꜛ):
            Ф₫ = Ϛꜛ
        υȼ += 1

    ξ₳ = 0

    def ωïc(sequence: str, acc: int) -> int:
        if sequence == "":
            return acc
        else:
            𝟼 = int(sequence[0])
            return ωïc(sequence[1:], acc + 𝟼)

    sum_of_digits = ωïc(str(Ф₫), 0)

    return sum_of_digits