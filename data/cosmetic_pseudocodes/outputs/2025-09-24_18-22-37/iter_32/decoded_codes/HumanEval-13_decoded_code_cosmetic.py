from typing import Union

def greatest_common_divisor(parameter_x: int, parameter_y: int) -> int:
    iterator_var: int = parameter_y

    while iterator_var != 0:
        swapped_var: int = iterator_var
        iterator_var = parameter_x - ((parameter_x // iterator_var) * iterator_var)
        parameter_x = swapped_var

    return parameter_x