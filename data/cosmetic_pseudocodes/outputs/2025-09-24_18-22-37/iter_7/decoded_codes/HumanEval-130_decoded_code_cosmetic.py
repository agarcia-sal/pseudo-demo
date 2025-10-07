from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n != 0:
        result_list: List[int] = [1, 3]
        index_var: int = 2
        while index_var <= integer_n:
            mod_result = index_var % 2
            if mod_result == 0:
                half_value = index_var // 2
                append_value = half_value + 1
            else:
                first_term = result_list[index_var - 1]
                second_term = result_list[index_var - 2]
                numerator = index_var + 3
                third_term = numerator // 2
                append_value = first_term + second_term + third_term
            result_list.append(append_value)
            index_var += 1
        return result_list
    else:
        return [1]