from typing import List


def f(integer_n: int) -> List[int]:
    aggregated_results: List[int] = []
    outer_counter: int = 1
    while outer_counter <= integer_n:
        if outer_counter % 2 != 1:  # even number
            acc_factorial: int = 1
            inner_counter: int = 1
            while inner_counter <= outer_counter:
                acc_factorial *= inner_counter
                inner_counter += 1
            aggregated_results.append(acc_factorial)
        else:
            acc_sum: int = 0
            inner_counter: int = 1
            while inner_counter <= outer_counter:
                acc_sum += inner_counter
                inner_counter += 1
            aggregated_results.append(acc_sum)
        outer_counter += 1
    return aggregated_results