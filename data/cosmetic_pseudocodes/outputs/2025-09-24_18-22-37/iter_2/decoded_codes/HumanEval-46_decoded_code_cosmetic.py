from typing import List

def fib4(integer_n: int) -> int:
    sequence: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return sequence[integer_n]

    idx: int = 4
    while idx <= integer_n:
        sum_last_four: int = sum(sequence)
        sequence.append(sum_last_four)
        sequence.pop(0)
        idx += 1

    return sequence[-1]