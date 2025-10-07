from typing import List, Any

def sort_even(list_of_elements: List[Any]) -> List[Any]:
    indexes_for_even: int = 0
    collected_even: List[Any] = []
    while indexes_for_even < len(list_of_elements):
        collected_even.append(list_of_elements[indexes_for_even])
        indexes_for_even += 2

    step: int = 1
    collected_odd: List[Any] = []
    while step < len(list_of_elements):
        collected_odd.append(list_of_elements[step])
        step += 2

    collected_even.sort()

    merged_result: List[Any] = []
    idx: int = 0
    while idx < len(collected_odd) and idx < len(collected_even):
        merged_result.append(collected_even[idx])
        merged_result.append(collected_odd[idx])
        idx += 1

    if len(collected_even) > len(collected_odd):
        merged_result.append(collected_even[-1])

    return merged_result