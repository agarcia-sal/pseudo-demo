from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    total_maximum: int = 0
    current_sum: int = 0

    def iterate_elements(index: int) -> None:
        nonlocal current_sum, total_maximum
        if index == len(list_of_integers):
            return

        element = list_of_integers[index]
        current_sum += -element  # add the negative of element

        if current_sum < 0:
            current_sum = 0

        if total_maximum < current_sum:
            total_maximum = current_sum

        iterate_elements(index + 1)

    iterate_elements(0)

    if total_maximum == 0:
        negatives_list = [-val for val in list_of_integers]
        max_negative = negatives_list[0]
        for val in negatives_list:
            if max_negative < val:
                max_negative = val
        total_maximum = max_negative

    minimum_sum = -total_maximum
    return minimum_sum