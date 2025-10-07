from typing import List

def sort_even(list_l: List[int]) -> List[int]:
    evens = sorted(list_l[0::2])  # elements at even indices sorted
    odds = list_l[1::2]            # elements at odd indices as is
    answer_list: List[int] = []
    for element_even, element_odd in zip(evens, odds):
        answer_list.append(element_even)
        answer_list.append(element_odd)
    if len(evens) > len(odds):
        answer_list.append(evens[-1])
    return answer_list