from typing import List, Any

def find_max(array_of_terms: List[List[Any]]) -> List[Any]:
    def recursive_sort(index: int, array_ref: List[List[Any]]) -> List[List[Any]]:
        if index >= len(array_ref) - 1:
            return array_ref
        swap_flag = False
        for position in range(len(array_ref) - 1):
            current_item = array_ref[position]
            next_item = array_ref[position + 1]
            current_unique_count = len(set(current_item))
            next_unique_count = len(set(next_item))
            if (current_unique_count < next_unique_count) or (current_unique_count == next_unique_count and current_item > next_item):
                array_ref[position], array_ref[position + 1] = next_item, current_item
                swap_flag = True
        if not swap_flag:
            return array_ref
        return recursive_sort(index + 1, array_ref)
    sorted_terms = recursive_sort(0, array_of_terms)
    return sorted_terms[0]