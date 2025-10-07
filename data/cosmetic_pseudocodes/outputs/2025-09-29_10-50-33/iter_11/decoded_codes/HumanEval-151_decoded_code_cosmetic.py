from typing import List

def double_the_difference(list_of_numbers: List[int]) -> int:
    index_counter: int = 0
    aggregate_sum: int = 0

    while index_counter < len(list_of_numbers):
        current_element: int = list_of_numbers[index_counter]

        # Check if current_element is positive, odd, and an integer without a decimal point
        if not (current_element <= 0 or current_element % 2 == 0 or '.' in str(current_element)):
            aggregate_sum += current_element * current_element

        index_counter += 1

    return aggregate_sum