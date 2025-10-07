from typing import List


def exchange(array_alpha: List[int], array_beta: List[int]) -> str:
    def sum_odd_alpha(index: int, accumulator: int) -> int:
        if index >= len(array_alpha):
            return accumulator
        if array_alpha[index] % 2 == 1:
            return sum_odd_alpha(index + 1, accumulator + 1)
        return sum_odd_alpha(index + 1, accumulator)

    def sum_even_beta(index: int, accumulator: int) -> int:
        if index >= len(array_beta):
            return accumulator
        if array_beta[index] % 2 == 0:
            return sum_even_beta(index + 1, accumulator + 1)
        return sum_even_beta(index + 1, accumulator)

    total_odd = sum_odd_alpha(0, 0)
    total_even = sum_even_beta(0, 0)

    if total_even >= total_odd:
        return "YES"
    return "NO"