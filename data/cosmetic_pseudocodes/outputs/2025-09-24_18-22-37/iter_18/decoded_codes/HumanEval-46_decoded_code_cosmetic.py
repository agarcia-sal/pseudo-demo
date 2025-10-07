from typing import List

def fib4(integer_n: int) -> int:
    intermediate: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return intermediate[integer_n]

    index_var: int = 4
    while index_var <= integer_n:
        temp_sum: int = sum(intermediate)  # sum of all four elements
        intermediate.append(temp_sum)
        intermediate.pop(0)  # remove the oldest element to maintain size 4
        index_var += 1

    return intermediate[3]