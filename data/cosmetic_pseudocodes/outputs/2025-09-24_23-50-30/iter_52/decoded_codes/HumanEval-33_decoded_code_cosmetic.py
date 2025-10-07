from typing import List, TypeVar

T = TypeVar('T', bound=object)

def sort_third(list_input: List[T]) -> List[T]:
    def replace_at_indices(
        input_list: List[T], 
        indices_list: List[int], 
        replacements_list: List[T], 
        current_index: int
    ) -> List[T]:
        if current_index == len(indices_list):
            return input_list
        pos = indices_list[current_index]
        # Create a copy on first replacement to avoid mutating input_list beyond scope
        updated_list = input_list.copy() if current_index == 0 else input_list
        updated_list[pos] = replacements_list[current_index]
        return replace_at_indices(updated_list, indices_list, replacements_list, current_index + 1)

    def gather_indices(len_val: int, idx: int) -> List[int]:
        if idx >= len_val:
            return []
        return [idx] + gather_indices(len_val, idx + 3)

    new_list: List[T] = [element for element in list_input]

    indices = gather_indices(len(new_list), 0)

    def gather_elements_at_indices(
        lst: List[T], 
        idxs: List[int], 
        pos: int
    ) -> List[T]:
        if pos >= len(idxs):
            return []
        return [lst[idxs[pos]]] + gather_elements_at_indices(lst, idxs, pos + 1)

    extracted_values = gather_elements_at_indices(new_list, indices, 0)

    def insertion_sort(arr: List[T], n: int) -> List[T]:
        if n <= 1:
            return arr
        sorted_arr = insertion_sort(arr, n - 1)
        key = sorted_arr[n - 1]
        j = n - 2
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = key
        return sorted_arr

    sorted_values = insertion_sort(extracted_values, len(extracted_values))

    final_list = replace_at_indices(new_list, indices, sorted_values, 0)

    return final_list