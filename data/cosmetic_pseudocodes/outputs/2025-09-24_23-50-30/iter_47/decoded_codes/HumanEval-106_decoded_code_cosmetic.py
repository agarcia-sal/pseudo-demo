from typing import List

def f(integer_n: int) -> List[int]:
    aggregate_result: List[int] = []
    index_counter: int = 1
    while index_counter <= integer_n:
        if not (index_counter % 2 != 0):  # True when index_counter is even
            accumulator_factorial: int = 1
            factor_loop_var: int = 1
            while factor_loop_var <= index_counter:
                accumulator_factorial *= factor_loop_var
                factor_loop_var += 1
            aggregate_result.append(accumulator_factorial)
        else:  # index_counter is odd
            accumulator_sum: int = 0
            sum_loop_var: int = 1
            while sum_loop_var <= index_counter:
                accumulator_sum += sum_loop_var
                sum_loop_var += 1
            aggregate_result.append(accumulator_sum)
        index_counter += 1
    return aggregate_result