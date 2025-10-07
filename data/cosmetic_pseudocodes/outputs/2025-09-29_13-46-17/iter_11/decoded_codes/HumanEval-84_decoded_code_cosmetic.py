from typing import Iterator

def solve(integer_N: int) -> str:
    acc: int = 0
    temp_sum: int = 0

    def recursive_func(it: Iterator[str], end: str) -> int:
        nonlocal acc, temp_sum
        try:
            current = next(it)
        except StopIteration:
            return acc
        if current == end:
            return acc
        else:
            temp_sum = acc + ord(current)
            acc = temp_sum - 48
            return recursive_func(it, end)

    s = str(integer_N)
    it = iter(s)
    acc = recursive_func(it, s[-1])
    # slice off '0b' prefix from binary representation
    binary_repr = bin(acc)[2:]
    return binary_repr