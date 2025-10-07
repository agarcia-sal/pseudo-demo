from typing import List

def f(param_x: int) -> List[int]:
    result_accum: List[int] = []

    def compute_factorial(counter_a: int, acc_b: int) -> int:
        if counter_a > param_x:
            return acc_b
        else:
            return compute_factorial(counter_a + 1, acc_b * counter_a)

    def compute_sum(counter_c: int, acc_d: int) -> int:
        if counter_c > param_x:
            return acc_d
        else:
            return compute_sum(counter_c + 1, acc_d + counter_c)

    def process_index(current_e: int) -> None:
        if current_e > param_x:
            return
        if current_e % 2 != 1:  # current_e is even
            value_f = compute_factorial(1, 1)
        else:
            value_f = compute_sum(1, 0)
        result_accum.append(value_f)
        process_index(current_e + 1)

    process_index(1)
    return result_accum