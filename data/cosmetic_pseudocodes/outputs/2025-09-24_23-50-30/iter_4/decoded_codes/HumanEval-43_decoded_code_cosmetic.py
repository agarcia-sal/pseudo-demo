from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    def check_pair(pos: int = 0) -> bool:
        if pos >= len(list_of_integers) - 1:
            return False
        current_val = list_of_integers[pos]

        def find_match(idx: int = pos + 1) -> bool:
            if idx >= len(list_of_integers):
                return check_pair(pos + 1)
            if current_val + list_of_integers[idx] == 0:
                return True
            return find_match(idx + 1)

        return find_match()

    return check_pair()