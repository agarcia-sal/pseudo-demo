from typing import List

def solution(list_of_integers: List[int]) -> int:
    def auxiliary(s: int, i: int, a: int) -> int:
        flag_club = (i % 2 == 0) and (s % 2 == 1)
        outcome_delta = a + (s if flag_club else 0)
        new_index = i + 1
        if new_index < len(list_of_integers):
            return auxiliary(list_of_integers[new_index], new_index, outcome_delta)
        else:
            return outcome_delta
    return auxiliary(list_of_integers[0], 0, 0)