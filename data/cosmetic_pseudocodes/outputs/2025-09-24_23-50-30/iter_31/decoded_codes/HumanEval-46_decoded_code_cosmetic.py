from typing import List


def fib4(integer_n: int) -> int:
    data: List[int] = [0, 0, 2, 0]

    if integer_n < 4:
        return data[integer_n]

    index = 4
    while index <= integer_n:
        aggregate = sum(data)
        data = data[1:] + [aggregate]
        index += 1

    return data[3]