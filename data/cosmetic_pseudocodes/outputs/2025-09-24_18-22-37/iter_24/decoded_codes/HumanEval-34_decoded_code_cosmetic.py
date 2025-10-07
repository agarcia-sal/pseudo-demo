from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    distinct_collection: set[T] = set()
    index_counter: int = 0
    while index_counter < len(list_of_elements):
        curr_element = list_of_elements[index_counter]
        distinct_collection.add(curr_element)
        index_counter += 1

    intermediate_list: List[T] = []
    for item in distinct_collection:
        intermediate_list.append(item)

    swap_flag: bool = True
    while swap_flag:
        swap_flag = False
        sorting_index: int = 1
        while sorting_index < len(intermediate_list):
            if intermediate_list[sorting_index - 1] > intermediate_list[sorting_index]:
                temp_var = intermediate_list[sorting_index - 1]
                intermediate_list[sorting_index - 1] = intermediate_list[sorting_index]
                intermediate_list[sorting_index] = temp_var
                swap_flag = True
            sorting_index += 1

    final_output: List[T] = intermediate_list
    return final_output