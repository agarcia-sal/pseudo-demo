from typing import List

def fib4(integer_n: int) -> int:
    results_list: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return results_list[integer_n]

    for each_index in range(4, integer_n + 1):
        next_val = sum(results_list)
        results_list.append(next_val)
        results_list.pop(0)

    return results_list[-1]