from typing import List


def get_odd_collatz(x: int) -> List[int]:
    result_list: List[int]

    if x % 2 == 0:
        result_list = []
    else:
        result_list = [x]

    while True:
        if x > 1:
            if x % 2 == 0:
                x = x // 2  # integer division
            else:
                x = x * 3 + 1

            if x % 2 != 0:
                temp_int = x
                result_list.append(temp_int)
        else:
            break

    return sorted(result_list)