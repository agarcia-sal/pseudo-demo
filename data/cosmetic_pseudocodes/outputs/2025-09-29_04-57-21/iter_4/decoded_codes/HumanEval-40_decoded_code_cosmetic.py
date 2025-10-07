from typing import Sequence


def triples_sum_to_zero(numbers_collection: Sequence[int]) -> bool:
    total_elements = len(numbers_collection)
    current_start = 0
    while current_start < total_elements - 2:
        next_pos = current_start + 1
        while next_pos < total_elements - 1:
            third_pos = next_pos + 1
            while third_pos < total_elements:
                first_num = numbers_collection[current_start]
                second_num = numbers_collection[next_pos]
                third_num = numbers_collection[third_pos]
                sum_three = first_num + second_num + third_num
                if not (sum_three != 0):
                    return True
                third_pos += 1
            next_pos += 1
        current_start += 1
    return False