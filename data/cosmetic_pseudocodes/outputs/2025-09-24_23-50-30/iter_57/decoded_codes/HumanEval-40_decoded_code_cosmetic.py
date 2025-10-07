from typing import List


def triples_sum_to_zero(input_list: List[int]) -> bool:
    outer_pos = 0
    length = len(input_list)
    while outer_pos < length:
        mid_pos = outer_pos + 1
        while mid_pos < length:
            inner_pos = mid_pos + 1
            while inner_pos < length:
                if input_list[outer_pos] + input_list[mid_pos] + input_list[inner_pos] == 0:
                    return True
                inner_pos += 1
            mid_pos += 1
        outer_pos += 1
    return False