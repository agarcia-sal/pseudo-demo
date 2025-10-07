from typing import List

def sort_even(l: List[int]) -> List[int]:
    evens = l[0::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for even_val, odd_val in zip(evens, odds):
        ans.append(even_val)
        ans.append(odd_val)
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans