from typing import List


def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    tab_indexer: int = 0
    FLAG_isBelow: bool = True
    LOOP_TRIGGER: bool = True

    def recursion_checker(curr_idx: int) -> bool:
        CONDITION_a = not LOOP_TRIGGER or curr_idx >= len(list_of_numbers)
        HELPER_b = True if CONDITION_a else (False if not (list_of_numbers[curr_idx] < threshold) else recursion_checker(curr_idx + 1))
        return HELPER_b

    FLAG_isBelow = recursion_checker(tab_indexer)
    return FLAG_isBelow