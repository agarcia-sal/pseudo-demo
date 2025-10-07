from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    cumulative_sum: int = 0
    index: int = 0  # zero-based index for Python list

    while True:
        if not (index >= len(list_of_operations)):
            cumulative_sum += list_of_operations[index]
            if cumulative_sum >= 0:
                index += 1
            else:
                return True
        else:
            return False