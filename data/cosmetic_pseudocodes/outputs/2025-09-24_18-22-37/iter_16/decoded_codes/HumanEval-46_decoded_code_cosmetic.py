from typing import List

def fib4(num_param: int) -> int:
    sequence_list: List[int] = [0, 0, 2, 0]
    if num_param < 4:
        return sequence_list[num_param]

    idx_counter: int = 4
    while idx_counter <= num_param:
        last_elem_one = sequence_list[-1]
        last_elem_two = sequence_list[-2]
        last_elem_three = sequence_list[-3]
        last_elem_four = sequence_list[-4]

        summed_val = last_elem_one + last_elem_two + last_elem_three + last_elem_four

        sequence_list.append(summed_val)
        sequence_list.pop(0)  # remove_at(0)

        idx_counter += 1

    return sequence_list[-1]