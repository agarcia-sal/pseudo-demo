from typing import List

def fib4(integer_n: int) -> int:
    temp_list: List[int] = [0, 0, 2, 0]

    def recur(index: int, buffer: List[int]) -> int:
        if index > integer_n:
            return buffer[-1]
        calc_value = buffer[0] + buffer[1] + buffer[2] + buffer[3]
        return recur(index + 1, [buffer[1], buffer[2], buffer[3], calc_value])

    if integer_n < 4:
        return temp_list[integer_n]
    return recur(4, temp_list)