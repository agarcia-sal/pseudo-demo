from typing import List


def fruit_distribution(desc_string: str, count_total_fruits: int) -> int:
    nums_list: List[int] = []
    elems_iter: List[str] = desc_string.split(" ")
    idx_counter: int = 0
    while idx_counter < len(elems_iter):
        curr_elem: str = elems_iter[idx_counter]
        if "0" <= curr_elem <= "9":
            val_int: int = int(curr_elem)
            nums_list.append(val_int)
        idx_counter += 1
    sum_nums: int = 0
    for i_sum in range(len(nums_list)):
        sum_nums += nums_list[i_sum]
    result: int = count_total_fruits - sum_nums
    return result