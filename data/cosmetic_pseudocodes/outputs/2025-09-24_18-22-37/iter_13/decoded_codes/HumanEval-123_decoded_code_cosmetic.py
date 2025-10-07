from typing import List


def get_odd_collatz(x: int) -> List[int]:
    temp_num: int = x
    if temp_num % 2 == 0:
        result_list: List[int] = []
    else:
        result_list = [temp_num]

    while temp_num > 1:
        is_even: bool = (temp_num % 2 == 0)
        if is_even:
            temp_num //= 2
        else:
            multiplied: int = temp_num * 3
            incremented: int = multiplied + 1
            temp_num = incremented

        is_odd: bool = (temp_num % 2 == 1)
        if is_odd:
            temp_int: int = int(temp_num)
            result_list.append(temp_int)

    sorted_result: List[int] = sorted(result_list)
    return sorted_result