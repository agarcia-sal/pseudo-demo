from typing import List


def sort_third(list_input: List[int]) -> List[int]:
    temp_list: List[int] = [elem for elem in list_input]  # Copy input list

    collected_vals: List[int] = [temp_list[pos] for pos in range(len(temp_list)) if pos % 3 == 0]

    sorted_collected: List[int] = sorted(collected_vals)

    def replace_vals(i: int, vals_index: int) -> None:
        if i >= len(temp_list):
            return
        if i % 3 == 0:
            temp_list[i] = sorted_collected[vals_index]
            replace_vals(i + 1, vals_index + 1)
        else:
            replace_vals(i + 1, vals_index)

    replace_vals(0, 0)
    return temp_list