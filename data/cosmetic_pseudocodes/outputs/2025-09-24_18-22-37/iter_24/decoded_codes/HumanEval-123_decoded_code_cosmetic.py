from typing import List


def get_odd_collatz(n: int) -> List[int]:
    temp_flag: bool = (n % 2 == 0)
    temp_list: List[int] = [] if temp_flag else [n]

    while n > 1:
        temp_val1: int = n % 2
        if temp_val1 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        temp_val2: int = n % 2
        if temp_val2 != 0:
            temp_list.append(n)

    temp_res: List[int] = sorted(temp_list)
    return temp_res