from typing import List

def sort_even(list_l: List[int]) -> List[int]:
    evens = list_l[0::2]
    odds = list_l[1::2]
    evens.sort()
    ans: List[int] = []
    min_len = min(len(evens), len(odds))
    for index in range(min_len):
        ans.append(evens[index])
        ans.append(odds[index])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans