from typing import List


def multiply(x: int, y: int) -> int:
    list_a: List[int] = [x]
    list_b: List[int] = [y]
    num_m: int = 0
    num_n: int = 0
    res: int = 0

    for element in list_a:
        num_m = ((element % 10) + 10) % 10
        if num_m < 0:
            num_m = -num_m

    for element in list_b:
        num_n = ((element % 10) + 10) % 10
        if num_n < 0:
            num_n = -num_n

    res = num_m * num_n
    return res