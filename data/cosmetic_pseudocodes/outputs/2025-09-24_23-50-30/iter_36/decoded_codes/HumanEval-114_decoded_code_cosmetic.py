from typing import List

def minSubArraySum(source: List[int]) -> int:
    accumulator: int = 0
    best_value: int = 0
    for index in range(len(source)):
        accumulator += -source[index]
        if accumulator < 0:
            accumulator = 0
        if best_value < accumulator:
            best_value = accumulator
    if best_value == 0:
        negated_values = [-x for x in source]
        best_value = negated_values[0]
        for i in range(1, len(negated_values)):
            if best_value < negated_values[i]:
                best_value = negated_values[i]
    result = -best_value
    return result