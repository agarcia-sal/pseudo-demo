from typing import List

def sort_third(list_input: List[int]) -> List[int]:
    copied_list: List[int] = [item for item in list_input]

    positions: List[int] = [i for i in range(len(copied_list)) if i % 3 == 0]
    extracted_values: List[int] = [copied_list[pos] for pos in positions]

    sorted_subset: List[int] = []
    while extracted_values:
        min_val = extracted_values[0]
        min_idx = 0
        for j in range(1, len(extracted_values)):
            if extracted_values[j] < min_val:
                min_val = extracted_values[j]
                min_idx = j
        sorted_subset.append(min_val)
        extracted_values.pop(min_idx)

    for k, idx in enumerate(positions):
        copied_list[idx] = sorted_subset[k]

    return copied_list