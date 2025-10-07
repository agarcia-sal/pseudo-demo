from typing import List

def make_a_pile(parameter_alpha: int) -> List[int]:
    result_collection: List[int] = []
    counter_beta: int = 0
    while counter_beta < parameter_alpha:
        interim_delta: int = parameter_alpha + (2 * counter_beta)
        result_collection.append(interim_delta)
        counter_beta += 1
    return result_collection