from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_l: List[T]) -> List[T]:
    list_evens = list_l[0::2]
    list_odds = list_l[1::2]
    list_evens.sort()
    list_answer: List[T] = []
    for e_even, e_odd in zip(list_evens, list_odds):
        list_answer.extend((e_even, e_odd))
    if len(list_evens) > len(list_odds):
        list_answer.append(list_evens[-1])
    return list_answer