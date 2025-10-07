from typing import List

def tri(parameter_p: int) -> List[int]:
    if parameter_p == 0:
        return [1]
    variable_x: List[int] = [1, 3]
    counter_c: int = 2
    while counter_c <= parameter_p:
        condition_flag = counter_c % 2
        if condition_flag == 0:
            temp_val = counter_c // 2 + 1
            variable_x.append(temp_val)
        else:
            idx1 = counter_c - 1
            idx2 = counter_c - 2
            val1 = variable_x[idx1]
            val2 = variable_x[idx2]
            half_calc = (counter_c + 3) // 2
            combined_sum = val1 + val2 + half_calc
            variable_x.append(combined_sum)
        counter_c += 1
    return variable_x