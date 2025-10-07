from typing import List

def sort_even(list_input: List[int]) -> List[int]:
    evens = list_input[0::2]
    odds = list_input[1::2]
    evens.sort()
    answer_list: List[int] = []
    for element_even, element_odd in zip(evens, odds):
        answer_list.append(element_even)
        answer_list.append(element_odd)
    if len(evens) > len(odds):
        answer_list.append(evens[-1])
    return answer_list