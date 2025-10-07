from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def recursion_outer(idx_outer: int) -> bool:
        if idx_outer == len(list_of_numbers):
            return False
        def recursion_inner(idx_inner: int) -> bool:
            if idx_inner == len(list_of_numbers):
                return recursion_outer(idx_outer + 1)
            if idx_outer != idx_inner:
                diff = abs(list_of_numbers[idx_outer] - list_of_numbers[idx_inner])
                if diff < threshold_value:
                    return True
            return recursion_inner(idx_inner + 1)
        return recursion_inner(0)
    return recursion_outer(0)