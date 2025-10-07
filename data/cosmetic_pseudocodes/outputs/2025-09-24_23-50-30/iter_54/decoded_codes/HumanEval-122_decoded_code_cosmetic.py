from typing import List

def add_elements(list_of_numbers: List[int], k_value: int) -> int:
    def helper(index: int, accumulator: int) -> int:
        if index > k_value:
            return accumulator
        current_value = list_of_numbers[index]
        # Add current_value if its string representation length is not greater than 2
        if len(str(current_value)) <= 2:
            return helper(index + 1, accumulator + current_value)
        return helper(index + 1, accumulator)
    return helper(1, 0)