from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    index_counter: int = 0
    current_accumulator: int = 0
    largest_accumulator: int = 0

    while index_counter < len(list_of_integers):
        element_val = list_of_integers[index_counter]
        current_accumulator += -element_val
        if current_accumulator < 0:
            current_accumulator = 0
        if current_accumulator > largest_accumulator:
            largest_accumulator = current_accumulator
        index_counter += 1

    if largest_accumulator == 0:
        transformed_list = [-x for x in list_of_integers]
        largest_accumulator = transformed_list[0]
        for value in transformed_list[1:]:
            if value > largest_accumulator:
                largest_accumulator = value

    return -largest_accumulator