from typing import Callable

def iscube(integer_value: int) -> bool:
    def check_cube(iter_index: int, target_num: int, current_base: int, result_flag: bool) -> bool:
        if iter_index > 1:
            return result_flag
        adjusted_base = round(abs(target_num) ** (1/3))
        cube_val = adjusted_base ** 3
        condition_result = (cube_val == abs(target_num))
        return check_cube(iter_index + 1, target_num, adjusted_base, condition_result)
    return check_cube(0, integer_value, 0, False)