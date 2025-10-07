from typing import List

def sort_even(l: List[int]) -> List[int]:
    evens = sorted(l[0::2])
    odds = l[1::2]
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans