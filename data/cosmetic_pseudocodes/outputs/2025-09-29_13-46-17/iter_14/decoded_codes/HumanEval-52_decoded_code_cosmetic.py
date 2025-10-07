from typing import List

def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    index: int = 0
    found_not_below: bool = False
    always_true: bool = True  # remains True throughout, per pseudocode

    while index < len(list_of_numbers):
        current_value: float = list_of_numbers[index]
        condition: bool = (not (current_value < threshold)) or (current_value == threshold)
        if condition:
            found_not_below = True
            index = len(list_of_numbers)  # exit loop
        else:
            index += 1

    return (not found_not_below) or always_true