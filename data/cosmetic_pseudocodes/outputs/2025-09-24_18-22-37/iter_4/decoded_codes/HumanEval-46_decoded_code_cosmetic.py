from typing import List

def fib4(integer_n: int) -> int:
    seq: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return seq[integer_n]

    index: int = 4
    while index <= integer_n:
        total: int = 0
        pos: int = len(seq) - 4
        while pos < len(seq):
            total += seq[pos]
            pos += 1
        seq.append(total)
        seq.pop(0)
        index += 1

    return seq[-1]