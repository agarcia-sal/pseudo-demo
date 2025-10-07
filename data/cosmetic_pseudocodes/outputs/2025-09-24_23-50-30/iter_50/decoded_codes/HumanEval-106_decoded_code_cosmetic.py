from typing import List

def f(integer_n: int) -> List[int]:
    def compute_factorial(tally: int, count: int, limit: int) -> int:
        if count > limit:
            return tally
        return compute_factorial(tally * count, count + 1, limit)

    def compute_sum(accumulate: int, index: int, max_index: int) -> int:
        if index > max_index:
            return accumulate
        return compute_sum(accumulate + index, index + 1, max_index)

    def iterate(current: int, end_limit: int, collected: List[int]) -> List[int]:
        if current > end_limit:
            return collected
        if current % 2 != 0:
            new_value = compute_sum(0, 1, current)
        else:
            new_value = compute_factorial(1, 1, current)
        return iterate(current + 1, end_limit, collected + [new_value])

    return iterate(1, integer_n, [])