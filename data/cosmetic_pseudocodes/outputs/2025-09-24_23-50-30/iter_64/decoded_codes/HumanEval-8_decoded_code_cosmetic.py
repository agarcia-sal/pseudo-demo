from typing import List, Tuple

def sum_product(shadowed_parameter: List[int]) -> Tuple[int, int]:
    temp_var_one: int = 0
    temp_var_two: int = 1

    def loop_over(index: int) -> Tuple[int, int]:
        nonlocal temp_var_one, temp_var_two
        if index >= len(shadowed_parameter):
            return (temp_var_one, temp_var_two)
        temp_var_one += shadowed_parameter[index]
        temp_var_two *= shadowed_parameter[index]
        return loop_over(index + 1)

    return loop_over(0)