from typing import List


def tri(integer_n: int) -> List[int]:
    result_list: List[int] = [1]
    if integer_n != 0:
        result_list = [1, 3]
        loop_counter: int = 2
        while loop_counter <= integer_n:
            is_even_flag: bool = (loop_counter % 2) == 0
            if is_even_flag:
                temp_val_1: int = (loop_counter // 2) + 1
                result_list.append(temp_val_1)
            else:
                temp_val_1 = result_list[loop_counter - 1]
                temp_val_2 = result_list[loop_counter - 2]
                temp_sum = (loop_counter + 3) // 2
                temp_val_1 += temp_val_2 + temp_sum
                result_list.append(temp_val_1)
            loop_counter += 1
    return result_list