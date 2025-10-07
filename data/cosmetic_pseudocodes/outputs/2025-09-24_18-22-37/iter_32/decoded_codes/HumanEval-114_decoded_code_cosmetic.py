from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    aggregate_maximum: int = 0
    rolling_accumulator: int = 0
    iterator_index: int = 0

    while iterator_index < len(list_of_integers):
        current_element: int = list_of_integers[iterator_index]
        rolling_accumulator += 0 - current_element  # accumulating negative of current_element
        if rolling_accumulator < 0:
            rolling_accumulator = 0
        if rolling_accumulator > aggregate_maximum:
            aggregate_maximum = rolling_accumulator
        iterator_index += 1

    if aggregate_maximum == 0:
        negative_elements: List[int] = [0 - element for element in list_of_integers]
        temp_maximum: int = negative_elements[0]
        neg_index: int = 1
        while neg_index < len(negative_elements):
            if negative_elements[neg_index] > temp_maximum:
                temp_maximum = negative_elements[neg_index]
            neg_index += 1
        aggregate_maximum = temp_maximum

    computed_minimum: int = 0 - aggregate_maximum
    return computed_minimum