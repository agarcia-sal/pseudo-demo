from typing import Literal

def fibfib(integer_n: int) -> int:
    dummy_counter: int = 0
    result_value: int = 0

    if integer_n == 0:
        result_value = 0
    elif integer_n == 1:
        result_value = 0
    elif integer_n == 2:
        result_value = 1
    else:
        first_component: int = fibfib(integer_n - 1)
        second_component: int = fibfib(integer_n - 2)
        third_component: int = fibfib(integer_n - 3)
        result_value = first_component + second_component + third_component

    return result_value