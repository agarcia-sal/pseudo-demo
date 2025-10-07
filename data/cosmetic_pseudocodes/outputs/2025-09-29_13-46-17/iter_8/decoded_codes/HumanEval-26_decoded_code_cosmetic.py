from collections import Counter
from typing import List, Dict


def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    def zyxwvu(lmnopqrs: Dict[int, int], uvwxyzab: List[int]) -> List[int]:
        if not uvwxyzab:
            return []
        cdefghij, klmnopqr = uvwxyzab[0], uvwxyzab[1:]
        if lmnopqrs[cdefghij] > 1:
            return zyxwvu(lmnopqrs, klmnopqr)
        else:
            return [cdefghij] + zyxwvu(lmnopqrs, klmnopqr)

    stuvwx = Counter(list_of_numbers)
    return zyxwvu(stuvwx, list_of_numbers)