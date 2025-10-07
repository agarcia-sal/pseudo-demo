from typing import List

def double_the_difference(list_of_numbers: List[float]) -> float:
    result_container: float = 0
    index_counter: int = 0
    while index_counter < len(list_of_numbers):
        candidate = list_of_numbers[index_counter]
        # Check candidate is positive integer (no decimal part), odd
        if not (candidate <= 0 or int(candidate) % 2 == 0 or ('.' in str(candidate))):
            result_container += candidate * candidate
            break
        index_counter += 1
    return result_container