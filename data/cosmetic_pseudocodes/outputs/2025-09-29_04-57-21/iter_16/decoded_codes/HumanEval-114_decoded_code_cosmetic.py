from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    aggregate_maximum: int = 0
    running_total: int = 0

    iterator = iter(list_of_integers)
    for current_value in iterator:
        running_total += -current_value
        if running_total < 0:
            running_total = 0
        if running_total > aggregate_maximum:
            aggregate_maximum = running_total

    if aggregate_maximum == 0:
        negations = [-element for element in list_of_integers]
        aggregate_maximum = max(negations)

    final_minimum = -aggregate_maximum
    return final_minimum