from typing import Sequence

def triples_sum_to_zero(numbers_collection: Sequence[int]) -> bool:
    length = len(numbers_collection)
    outer_index = 0
    while outer_index <= length - 1:
        middle_index = outer_index + 1
        while middle_index <= length - 1:
            inner_index = middle_index + 1
            while inner_index <= length - 1:
                first_value = numbers_collection[outer_index]
                second_value = numbers_collection[middle_index]
                third_value = numbers_collection[inner_index]
                total_sum = first_value + second_value + third_value
                if total_sum == 0:
                    return True
                inner_index += 1
            middle_index += 1
        outer_index += 1
    return False