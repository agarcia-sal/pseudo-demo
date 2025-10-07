from typing import List


def fib4(integer_n: int) -> int:
    sequence: List[int] = [0, 0, 2, 0]

    if integer_n < 4:
        return sequence[integer_n]

    counter: int = 4
    while counter <= integer_n:
        sum_of_last_four: int = sum(sequence)
        sequence.append(sum_of_last_four)
        del sequence[0]
        counter += 1

    return sequence[-1]