from typing import List


def f(integer_n: int) -> List[int]:
    def helper(accumulator: int, counter: int, boundary: int) -> int:
        if counter > boundary:
            return accumulator
        return helper(accumulator * counter, counter + 1, boundary)

    def helper_sum(accumulator_sum: int, counter_sum: int, boundary_sum: int) -> int:
        if counter_sum > boundary_sum:
            return accumulator_sum
        return helper_sum(accumulator_sum + counter_sum, counter_sum + 1, boundary_sum)

    collection: List[int] = []

    def loop(index: int) -> None:
        if index > integer_n:
            return
        if index % 2 == 0:
            val = helper(1, 1, index)
            collection.append(val)
        else:
            val_alt = helper_sum(0, 1, index)
            collection.append(val_alt)
        loop(index + 1)

    loop(1)
    return collection