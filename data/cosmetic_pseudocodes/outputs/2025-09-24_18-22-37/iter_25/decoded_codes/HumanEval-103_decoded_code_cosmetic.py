from math import floor, ceil
from typing import Union


def rounded_avg(alpha: int, beta: int) -> str:
    if beta < alpha:
        return "-1"

    sum_container: int = 0
    count_measure: int = (beta - alpha) + 1
    index_pointer: int = alpha

    while True:
        if index_pointer > beta:
            break
        sum_container += index_pointer
        index_pointer += 1

    average_calc: float = sum_container / count_measure

    temp_var1: float = average_calc - floor(average_calc)
    temp_var2: int
    if temp_var1 >= 0.5:
        temp_var2 = ceil(average_calc)
    else:
        temp_var2 = floor(average_calc)

    binary_string: str = ""
    number_to_convert: int = temp_var2

    if number_to_convert == 0:
        binary_string = "0"
    else:
        buffer_list = []
        while number_to_convert != 0:
            temp_digit = number_to_convert % 2
            buffer_list.insert(0, str(temp_digit))
            number_to_convert = (number_to_convert - temp_digit) // 2

        for element in buffer_list:
            binary_string += element

    return binary_string