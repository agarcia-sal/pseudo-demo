from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    idx: int = 0
    while idx < len(list_of_integers):
        nxt: int = idx + 1
        while nxt < len(list_of_integers):
            if (list_of_integers[idx] + list_of_integers[nxt]) == 0:
                return True
            nxt += 1
        idx += 1
    return False