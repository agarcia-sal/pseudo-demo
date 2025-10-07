from typing import List


def minSubArraySum(list_of_integers: List[int]) -> int:
    highest_partial_sum: int = 0
    accumulating_sum: int = 0
    iterator: int = 0
    while iterator < len(list_of_integers):
        current_element: int = list_of_integers[iterator]
        accumulating_sum += -current_element
        if accumulating_sum < 0:
            accumulating_sum = 0
        if highest_partial_sum < accumulating_sum:
            highest_partial_sum = accumulating_sum
        iterator += 1

    if highest_partial_sum == 0:
        negative_values: List[int] = [-element for element in list_of_integers]
        highest_partial_sum = negative_values[0]
        index_counter: int = 1
        while index_counter < len(negative_values):
            if highest_partial_sum < negative_values[index_counter]:
                highest_partial_sum = negative_values[index_counter]
            index_counter += 1

    return -highest_partial_sum