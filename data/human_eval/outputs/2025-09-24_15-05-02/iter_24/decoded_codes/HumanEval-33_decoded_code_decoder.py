from typing import List, Union, Sequence

def sort_third(list_l: Sequence[Union[int, float]]) -> List[Union[int, float]]:
    list_copy = list(list_l)  # Convert input to list to allow modifications
    indices = range(0, len(list_copy), 3)
    elements_at_multiples_of_three = [list_copy[i] for i in indices]
    elements_at_multiples_of_three.sort()
    for idx, sorted_value in zip(indices, elements_at_multiples_of_three):
        list_copy[idx] = sorted_value
    return list_copy