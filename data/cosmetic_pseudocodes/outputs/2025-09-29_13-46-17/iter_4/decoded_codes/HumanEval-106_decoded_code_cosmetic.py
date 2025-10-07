from typing import List

def f(n_val: int) -> List[int]:
    def calculate_factorial(accumulator: int, counter: int, limit: int) -> int:
        if counter > limit:
            return accumulator
        return calculate_factorial(accumulator * counter, counter + 1, limit)

    def calculate_sum(accumulated_sum: int, current: int, end: int) -> int:
        if current > end:
            return accumulated_sum
        return calculate_sum(accumulated_sum + current, current + 1, end)

    output_array: List[int] = []

    def loop_through(index: int) -> None:
        if index > n_val:
            return
        if not (index % 2 != 0):  # index even
            factorial_result = calculate_factorial(1, 1, index)
            output_array.append(factorial_result)
        else:
            sum_result = calculate_sum(0, 1, index)
            output_array.append(sum_result)
        loop_through(index + 1)

    loop_through(1)
    return output_array