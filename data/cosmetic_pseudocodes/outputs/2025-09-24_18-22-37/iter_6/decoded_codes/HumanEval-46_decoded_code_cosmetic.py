from typing import List


def fib4(integer_n: int) -> int:
    seq: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return seq[integer_n]

    counter: int = 4
    while counter <= integer_n:
        temp_sum: int = seq[-1] + seq[-2] + seq[-3] + seq[-4]
        seq.append(temp_sum)
        seq.pop(0)
        counter += 1

    return seq[-1]