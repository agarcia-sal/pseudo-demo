from typing import List

def solution(list_of_integers: List[int]) -> int:
    running_total: int = 0
    position_counter: int = 0
    while position_counter < len(list_of_integers):
        candidate_value = list_of_integers[position_counter]
        if (position_counter % 2 == 0) and (candidate_value % 2 == 1):
            running_total += candidate_value
        position_counter += 1
    return running_total