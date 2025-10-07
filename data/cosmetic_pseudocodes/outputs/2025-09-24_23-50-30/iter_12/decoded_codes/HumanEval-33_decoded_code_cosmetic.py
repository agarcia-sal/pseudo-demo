from typing import List, Sequence

def sort_third(list_input: Sequence[int]) -> List[int]:
    temp_list: List[int] = list(list_input)
    indices_multiple_three: List[int] = [i for i in range(len(temp_list)) if i % 3 == 0]
    extracted_values: List[int] = [temp_list[i] for i in indices_multiple_three]
    ordered_values: List[int] = sorted(extracted_values)
    for k in range(len(indices_multiple_three)):
        idx = indices_multiple_three[k]
        temp_list[idx] = ordered_values[k]
    return temp_list