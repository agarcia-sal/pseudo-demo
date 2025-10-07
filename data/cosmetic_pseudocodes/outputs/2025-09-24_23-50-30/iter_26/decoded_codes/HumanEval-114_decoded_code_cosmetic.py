from typing import List

def minSubArraySum(array_of_values: List[int]) -> int:
    acc_max: int = 0
    acc_temp: int = 0

    def process_elements(index: int) -> int:
        nonlocal acc_max, acc_temp
        if index >= len(array_of_values):
            return acc_max
        current_element = array_of_values[index]
        acc_temp += 0 - current_element  # accumulate negated current_element
        acc_temp = max(acc_temp, 0)
        acc_max = max(acc_max, acc_temp)
        return process_elements(index + 1)

    acc_max = process_elements(0)

    if acc_max == 0:
        acc_max = max((-v for v in array_of_values))

    return 0 - acc_max