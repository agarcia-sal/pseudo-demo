from typing import List

def sort_even(list_l: List[int]) -> List[int]:
    list_evens = list_l[0::2]
    list_odds = list_l[1::2]
    list_evens.sort()
    list_ans: List[int] = []
    for element_e, element_o in zip(list_evens, list_odds):
        list_ans.append(element_e)
        list_ans.append(element_o)
    if len(list_evens) > len(list_odds):
        list_ans.append(list_evens[-1])
    return list_ans