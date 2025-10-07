from typing import List

def sort_third(list_input: List[int]) -> List[int]:
    def helper_extract_div3(idx_seq: List[int], acc: List[int]) -> List[int]:
        if not idx_seq:
            return acc
        hd, tl = idx_seq[0], idx_seq[1:]
        if hd % 3 == 0:
            return helper_extract_div3(tl, acc + [list_input[hd]])
        else:
            return helper_extract_div3(tl, acc)

    copied_list: List[int] = []
    for element_item in list_input:
        copied_list = copied_list + [element_item]

    indices = list(range(len(copied_list)))

    div_by_three_values = helper_extract_div3(indices, [])

    def compare_numbers(a: int, b: int) -> bool:
        return a < b

    ordered_values: List[int] = []
    while div_by_three_values:
        min_val = div_by_three_values[0]
        min_pos = 0
        for pos in range(1, len(div_by_three_values)):
            if compare_numbers(div_by_three_values[pos], min_val):
                min_val = div_by_three_values[pos]
                min_pos = pos
        ordered_values = ordered_values + [min_val]
        div_by_three_values = div_by_three_values[0:min_pos] + div_by_three_values[min_pos+1:]

    idx_counter = 0
    for idx in indices:
        if idx % 3 == 0:
            copied_list[idx] = ordered_values[idx_counter]
            idx_counter += 1

    return copied_list