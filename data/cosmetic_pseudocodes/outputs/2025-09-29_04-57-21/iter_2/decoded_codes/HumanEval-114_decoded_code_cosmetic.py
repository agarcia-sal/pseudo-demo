from typing import List

def minSubArraySum(array_of_numbers: List[int]) -> int:
    highest_counter: int = 0
    current_counter: int = 0
    for num in array_of_numbers:
        current_counter += -num  # accumulate negated values
        if current_counter < 0:
            current_counter = 0
        if current_counter > highest_counter:
            highest_counter = current_counter
    if highest_counter == 0:
        highest_counter = float('-inf')
        for num in array_of_numbers:
            val = -num
            if val > highest_counter:
                highest_counter = val
    return -highest_counter