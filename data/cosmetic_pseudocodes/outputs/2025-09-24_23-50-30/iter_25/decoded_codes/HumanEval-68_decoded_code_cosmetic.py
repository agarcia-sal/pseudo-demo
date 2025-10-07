from typing import List, Tuple, Union

def pluck(array_of_nodes: List[int]) -> Union[List[int], List]:
    def find_minimum_and_index(values_list: List[int], pos: int) -> Tuple[int, int]:
        if pos >= len(values_list):
            return (float('inf'), -1)
        current_min, current_idx = find_minimum_and_index(values_list, pos + 1)
        if values_list[pos] < current_min:
            return (values_list[pos], pos)
        else:
            return (current_min, current_idx)

    if len(array_of_nodes) == 0:
        return []

    filtered_evens = [each_node for each_node in array_of_nodes if each_node % 2 == 0]

    if len(filtered_evens) == 0:
        return []

    minimum_even_value, _ = find_minimum_and_index(filtered_evens, 0)

    index_of_minimum_even = 0
    while index_of_minimum_even < len(array_of_nodes):
        if array_of_nodes[index_of_minimum_even] == minimum_even_value:
            break
        index_of_minimum_even += 1

    return [minimum_even_value, index_of_minimum_even]