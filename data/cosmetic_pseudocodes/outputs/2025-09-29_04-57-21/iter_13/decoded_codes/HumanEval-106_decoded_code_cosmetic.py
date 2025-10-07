from typing import List

def f(integer_n: int) -> List[int]:
    output_sequence: List[int] = []

    def compute_factorial(current_num: int, accumulator: int) -> int:
        if current_num > 0:
            return compute_factorial(current_num - 1, accumulator * current_num)
        else:
            return accumulator

    def compute_sum(limit: int) -> int:
        return (limit * (limit + 1)) // 2

    def process(index: int) -> None:
        if index > integer_n:
            return
        if index % 2 != 1:
            factorial_result = compute_factorial(index, 1)
            output_sequence.append(factorial_result)
            process(index + 1)
            return
        sum_result = compute_sum(index)
        output_sequence.append(sum_result)
        process(index + 1)

    process(1)
    return output_sequence