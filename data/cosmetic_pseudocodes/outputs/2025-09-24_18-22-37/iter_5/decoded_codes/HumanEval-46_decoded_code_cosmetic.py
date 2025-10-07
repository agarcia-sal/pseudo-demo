from typing import List

def fib4(number_m: int) -> int:
    temp_list: List[int] = [0, 0, 2, 0]
    if number_m < 4:
        return temp_list[number_m]

    counter: int = 4
    while counter <= number_m:
        sum_last_four = sum(temp_list)
        temp_list.append(sum_last_four)
        temp_list.pop(0)
        counter += 1

    return temp_list[-1]