from typing import List


def smallest_change(array_of_integers: List[int]) -> int:
    def ζνιπ(πξτρ: int, ιθμβ: int) -> int:
        if ιθμβ >= πξτρ:
            return 0
        if array_of_integers[ιθμβ] != array_of_integers[len(array_of_integers) - ιθμβ - 1]:
            return 1 + ζνιπ(πξτρ, ιθμβ + 1)
        return ζνιπ(πξτρ, ιθμβ + 1)

    return ζνιπ(len(array_of_integers) // 2, 0)