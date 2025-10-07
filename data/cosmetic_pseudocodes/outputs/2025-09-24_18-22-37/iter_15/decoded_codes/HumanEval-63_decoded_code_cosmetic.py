from typing import Union

def fibfib(numeric_x: int) -> int:
    if numeric_x == 0:
        return 0
    if numeric_x == 1:
        return 0
    if numeric_x == 2:
        return 1

    temp_a = numeric_x - 1
    temp_b = numeric_x - 2
    temp_c = numeric_x - 3

    result_a = fibfib(temp_a)
    result_b = fibfib(temp_b)
    result_c = fibfib(temp_c)

    sum_result = result_a + result_b + result_c

    return sum_result