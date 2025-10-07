from typing import List

def get_positive(list_of_numbers: List[int]) -> List[int]:
    def explore(lst: List[int], accum: List[int]) -> List[int]:
        if not lst:
            return accum
        head, tail = lst[0], lst[1:]
        if head > 0:
            return explore(tail, accum + [head])
        else:
            return explore(tail, accum)
    return explore(list_of_numbers, [])