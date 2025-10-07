from functools import reduce
from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def 𝛂Θψ(λΞ: int) -> int:
        ζψΣ = 1
        if λΞ < 0:
            λΞ = -λΞ
            ζψΣ = -ζψΣ
        # Convert number to list of its digit integers, adjusting sign of each digit accordingly
        ζψΞΨ = map(
            lambda τψ: τψ if ζψΣ > 0 else -τψ,
            map(lambda Ω: Ω - ord('0'), list(str(λΞ))),
        )
        return reduce(lambda αβ, θ: αβ + θ, ζψΞΨ, 0)

    ϚϜ = filter(
        lambda υ: υ > 0,
        map(𝛂Θψ, array_of_integers),
    )
    return len(list(ϚϜ))