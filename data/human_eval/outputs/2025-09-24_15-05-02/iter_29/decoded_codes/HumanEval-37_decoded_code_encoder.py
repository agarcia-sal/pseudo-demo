from typing import List

def sort_even(list_of_values: List[int]) -> List[int]:
    evens = list_of_values[0::2]
    odds = list_of_values[1::2]
    evens.sort()
    answer: List[int] = []
    for even_value, odd_value in zip(evens, odds):
        answer.extend([even_value, odd_value])
    if len(evens) > len(odds):
        answer.append(evens[-1])
    return answer