from typing import List

def f(integer_n: int) -> List[int]:
    aggregation: List[int] = []

    def compute_factorial(current: int, limit: int, acc: int) -> int:
        if current > limit:
            return acc
        else:
            return compute_factorial(current + 1, limit, acc * current)

    def compute_sum(current: int, limit: int, acc: int) -> int:
        while current <= limit:
            acc += current
            current += 1
        return acc

    counter = 1
    while counter <= integer_n:
        if (counter % 2) != 1:
            aggregation.append(compute_factorial(1, counter, 1))
        else:
            aggregation.append(compute_sum(1, counter, 0))
        counter += 1

    return aggregation