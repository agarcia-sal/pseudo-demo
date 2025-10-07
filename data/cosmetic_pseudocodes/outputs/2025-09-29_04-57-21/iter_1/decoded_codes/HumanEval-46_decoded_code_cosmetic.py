from typing import List

def fib4(integer_n: int) -> int:
    sequence: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return sequence[integer_n]

    integer_i = 4
    while integer_i <= integer_n:
        next_term = sum(sequence)
        sequence.append(next_term)
        sequence.pop(0)
        integer_i += 1

    return sequence[-1]