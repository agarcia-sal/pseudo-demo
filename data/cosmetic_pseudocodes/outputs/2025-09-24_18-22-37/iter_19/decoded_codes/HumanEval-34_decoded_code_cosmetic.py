from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(collection_var: Iterable[T]) -> List[T]:
    unique_set = set()
    temp_list: List[T] = []

    # Collect unique elements preserving insertion into the set
    for index_var in range(len(collection_var)):  # Need to support indexing; input assumed to be indexable
        ele = collection_var[index_var]
        if ele not in unique_set:
            unique_set.add(ele)

    # Create a list from the set (order not preserved)
    for ele in unique_set:
        temp_list.append(ele)

    # Selection sort
    for j in range(len(temp_list)):
        min_index = j
        for k in range(j + 1, len(temp_list)):
            if temp_list[k] < temp_list[min_index]:
                min_index = k
        temp_list[j], temp_list[min_index] = temp_list[min_index], temp_list[j]

    sorted_list = temp_list
    return sorted_list