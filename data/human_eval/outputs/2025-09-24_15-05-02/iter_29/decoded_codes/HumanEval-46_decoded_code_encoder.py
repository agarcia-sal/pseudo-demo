from typing import List

def fib4(integer_n: int) -> int:
    list_of_results: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return list_of_results[integer_n]

    for each_index in range(4, integer_n + 1):
        list_of_results.append(sum(list_of_results[-4:]))
        list_of_results.pop(0)

    return list_of_results[-1]