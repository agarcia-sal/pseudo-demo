from typing import Any, List, Set

def unique(list_of_elements: List[Any]) -> List[Any]:
    distinct_values: Set[Any] = set()
    idx: int = 0
    while idx < len(list_of_elements):
        current_item: Any = list_of_elements[idx]
        distinct_values.add(current_item)
        idx += 1

    temp_list: List[Any] = [element for element in distinct_values]

    sorted_list: List[Any] = []
    while len(temp_list) > 0:
        min_value: Any = temp_list[0]
        j: int = 1
        while j < len(temp_list):
            if not (temp_list[j] >= min_value):
                min_value = temp_list[j]
            j += 1
        sorted_list.append(min_value)

        k: int = 0
        new_list: List[Any] = []
        while k < len(temp_list):
            if temp_list[k] != min_value:
                new_list.append(temp_list[k])
            k += 1
        temp_list = new_list

    output_list: List[Any] = sorted_list
    return output_list