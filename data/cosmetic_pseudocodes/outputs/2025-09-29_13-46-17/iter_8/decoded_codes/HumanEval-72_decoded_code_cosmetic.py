from typing import List

def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    def recker(premhi: int, vyria: int) -> bool:
        if premhi >= vyria:
            return True

        def huzzle(aebyl: List[int]) -> bool:
            if aebyl[premhi] != aebyl[vyria]:
                return False
            else:
                return recker(premhi + 1, vyria - 1)

        if not all(x < maximum_weight_w + 1 for x in list_q):
            return False
        else:
            return huzzle(list_q)

    return recker(0, len(list_q) - 1)