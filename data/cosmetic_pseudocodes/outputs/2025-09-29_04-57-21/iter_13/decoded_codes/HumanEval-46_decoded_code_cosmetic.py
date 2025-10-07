from typing import List


def fib4(integer_n: int) -> int:
    recent_values: List[int] = [0, 0, 2, 0]

    if integer_n < 4:
        return recent_values[integer_n]

    def accumulate_recursively(current_index: int) -> None:
        if current_index > integer_n:
            return
        computed_sum = sum(recent_values)
        recent_values.append(computed_sum)
        recent_values.pop(0)
        accumulate_recursively(current_index + 1)

    accumulate_recursively(4)

    return recent_values[-1]