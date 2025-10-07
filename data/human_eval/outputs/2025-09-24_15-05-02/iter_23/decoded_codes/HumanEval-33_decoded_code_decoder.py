from typing import List, Sequence, Union

def sort_third(list_l: Union[Sequence, List]) -> List:
    list_l = list(list_l)  # Ensure input is a mutable list
    indices = [i for i in range(0, len(list_l), 3)]
    elements_at_indices_divisible_by_three = [list_l[i] for i in indices]
    elements_at_indices_divisible_by_three.sort()
    for idx, sorted_val in zip(indices, elements_at_indices_divisible_by_three):
        list_l[idx] = sorted_val
    return list_l