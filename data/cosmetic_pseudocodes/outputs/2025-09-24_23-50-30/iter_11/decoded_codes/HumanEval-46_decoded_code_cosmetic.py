from typing import List

def fib4(integer_n: int) -> int:
    data: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return data[integer_n]
    i = 4
    while i <= integer_n:
        total = sum(data)
        data = data[1:] + [total]  # shift left and add total at the end
        i += 1
    return data[3]