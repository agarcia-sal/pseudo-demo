from typing import List

def sort_even(list_l: List[int]) -> List[int]:
    evens = sorted(list_l[0::2])
    odds = list_l[1::2]
    ans: List[int] = []
    for element_e, element_o in zip(evens, odds):
        ans.append(element_e)
        ans.append(element_o)
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans