from typing import List

def f(integer_n: int) -> List[int]:
    outcomes: List[int] = []

    def compute_factorial(limit: int, current: int, acc: int) -> int:
        if current > limit:
            return acc
        return compute_factorial(limit, current + 1, acc * current)

    def compute_sum(limit: int, current: int, total: int) -> int:
        if current > limit:
            return total
        return compute_sum(limit, current + 1, total + current)

    iterator = 1
    while iterator <= integer_n:
        if not (iterator % 2 != 0):
            factorial_result = compute_factorial(iterator, 1, 1)
            outcomes.append(factorial_result)
        else:
            sum_result = compute_sum(iterator, 1, 0)
            outcomes.append(sum_result)
        iterator += 1

    return outcomes