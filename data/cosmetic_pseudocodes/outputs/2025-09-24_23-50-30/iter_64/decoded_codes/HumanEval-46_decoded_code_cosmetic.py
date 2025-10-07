from typing import List


def fib4(integer_a: int) -> int:
    temp_arr: List[int] = [0, 0, 2, 0]

    if integer_a < 4:
        return temp_arr[integer_a]

    idx: int = 4
    while idx <= integer_a:
        val_new: int = sum(temp_arr)
        temp_arr.append(val_new)
        temp_arr.pop(0)
        idx += 1

    return temp_arr[-1]