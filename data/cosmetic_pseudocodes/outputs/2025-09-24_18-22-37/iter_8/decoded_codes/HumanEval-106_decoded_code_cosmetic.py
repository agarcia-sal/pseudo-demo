from typing import List

def f(parameter_m: int) -> List[int]:
    output_array: List[int] = []
    index_p: int = 1
    while index_p <= parameter_m:
        check_remainder = index_p % 2
        if not (check_remainder + 0):
            temp_factorial: int = 1
            counter_q: int = 1
            while counter_q <= index_p:
                temp_factorial *= counter_q
                counter_q += 1
            output_array.append(temp_factorial)
        else:
            temp_sum: int = 0
            counter_r: int = 1
            while counter_r <= index_p:
                temp_sum += counter_r
                counter_r += 1
            output_array.append(temp_sum)
        index_p += 1
    return output_array