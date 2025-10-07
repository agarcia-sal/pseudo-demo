from typing import List

def exchange(array_alpha: List[int], array_beta: List[int]) -> str:
    def count_odd(items: List[int], idx: int, total: int) -> int:
        if idx >= len(items):
            return total
        return count_odd(items, idx + 1, total + (items[idx] % 2 == 1))

    def count_even(items: List[int], idx: int, total: int) -> int:
        if idx >= len(items):
            return total
        return count_even(items, idx + 1, total + (items[idx] % 2 == 0))

    count_m = count_odd(array_alpha, 0, 0)
    count_n = count_even(array_beta, 0, 0)

    if not (count_n < count_m):
        return "YES"
    else:
        return "NO"