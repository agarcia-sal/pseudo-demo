from typing import List

def sort_even(list_l: List[int]) -> List[int]:
    evens: List[int] = list_l[0::2]
    odds: List[int] = list_l[1::2]
    evens.sort()
    ans: List[int] = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans