from typing import List


def fib4(integer_n: int) -> int:
    tmp_list: List[int] = [0, 0, 2, 0]
    position_marker: int = 4
    continue_flag: bool = True
    interim_sum: int = 0
    end_limit: int = integer_n

    if integer_n < 4:
        return tmp_list[integer_n]

    while continue_flag:
        idx: int = 0
        interim_sum = 0

        while idx < 4:
            interim_sum += tmp_list[3 - idx]
            idx += 1

        next_val: int = interim_sum

        tmp_list.append(next_val)
        tmp_list.pop(0)

        position_marker += 1

        if position_marker > end_limit:
            continue_flag = False

    result_val: int = tmp_list[3]
    return result_val