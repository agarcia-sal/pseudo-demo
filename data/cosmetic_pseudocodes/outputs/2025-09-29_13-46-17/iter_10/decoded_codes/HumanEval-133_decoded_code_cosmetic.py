from typing import List
import math

def sum_squares(list_of_numbers: List[float]) -> int:
    def helper(_: List[float], numbers: List[float]) -> int:
        if not numbers:
            return 0
        head = math.ceil(numbers[0])
        return head * head + helper(_, numbers[1:])
    return helper(list_of_numbers, list_of_numbers)