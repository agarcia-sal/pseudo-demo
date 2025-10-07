from typing import List

def fib4(integer_p: int) -> int:
    buffer_seq: List[int] = [0, 0, 2, 0]

    if integer_p < 4:
        return buffer_seq[integer_p]

    idx: int = 4
    while idx <= integer_p:
        acc: int = sum(buffer_seq)
        buffer_seq = [buffer_seq[1], buffer_seq[2], buffer_seq[3], acc]
        idx += 1

    return buffer_seq[3]