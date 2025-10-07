from typing import List

def sort_even(l: List[int]) -> List[int]:
    evens = l[0::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    zipped_pairs = list(zip(evens, odds))
    for e, o in zipped_pairs:
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans