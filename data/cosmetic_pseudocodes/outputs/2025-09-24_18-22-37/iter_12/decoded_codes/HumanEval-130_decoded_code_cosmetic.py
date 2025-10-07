from typing import List


def tri(param_x: int) -> List[int]:
    if param_x == 0:
        return [1]

    list_temp: List[int] = [1, 3]
    index_var: int = 2
    while index_var <= param_x:
        if index_var % 2 == 0:
            to_append = (index_var // 2) + 1
            list_temp.append(to_append)
        else:
            first_val = list_temp[index_var - 1]
            second_val = list_temp[index_var - 2]
            third_val = (index_var + 3) // 2
            sum_val = first_val + second_val + third_val
            list_temp.append(sum_val)
        index_var += 1

    return list_temp