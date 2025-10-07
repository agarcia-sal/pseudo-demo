from typing import List

def sort_even(l: List[int]) -> List[int]:
    evens: List[int] = l[0::2]
    odds: List[int] = l[1::2]
    evens.sort()
    ans: List[int] = []
    for e, o in zip(evens, odds):
        ans.append(e)
        ans.append(o)
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans