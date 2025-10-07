from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    result_list: List[int] = [1, 3]
    loop_index: int = 2

    while loop_index <= integer_n:
        remainder_mod = loop_index - (loop_index // 2) * 2

        if remainder_mod == 0:
            half_plus_one = (loop_index // 2) + 1
            result_list.append(half_plus_one)
        else:
            left_term = result_list[loop_index - 1]
            right_term = result_list[loop_index - 2]
            middle_term = (loop_index + 3) // 2
            sum_value = left_term + right_term + middle_term
            result_list.append(sum_value)

        loop_index += 1

    return result_list