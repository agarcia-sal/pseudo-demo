from typing import List

def f(param_n: int) -> List[int]:
    output_array: List[int] = []
    counter_x: int = 1
    while counter_x <= param_n:
        if counter_x % 2 == 0:
            temp_factorial: int = 1
            multiplier_y: int = 1
            while multiplier_y <= counter_x:
                temp_factorial *= multiplier_y
                multiplier_y += 1
            temp_result: int = temp_factorial
        else:
            temp_sum: int = 0
            for adder_z in range(1, counter_x + 1):
                temp_sum += adder_z
            temp_result: int = temp_sum
        output_array.append(temp_result)
        counter_x += 1
    return output_array