from typing import List

def fib4(integer_n: int) -> int:
    temp_list: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return temp_list[integer_n]

    idx: int = 4
    while idx <= integer_n:
        sum_last_four = sum(temp_list)
        temp_list.append(sum_last_four)
        del temp_list[0]
        idx += 1

    return temp_list[-1]