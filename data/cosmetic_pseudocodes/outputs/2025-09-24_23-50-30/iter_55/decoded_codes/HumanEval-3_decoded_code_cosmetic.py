from typing import List

def below_zero(array_of_events: List[int]) -> bool:
    def helper(index: int, accumulator: int) -> bool:
        if index >= len(array_of_events):
            return False
        updated_value: int = accumulator + array_of_events[index]
        if updated_value < 0:
            return True
        else:
            return helper(index + 1, updated_value)
    return helper(0, 0)