from typing import List, Optional

def pluck(nodes_collection: List[int]) -> List[int]:
    if not nodes_collection:
        return []

    def collect_evens(src_nodes: List[int], evens_accum: List[int], pos: int) -> List[int]:
        if pos == len(src_nodes):
            return evens_accum
        if src_nodes[pos] % 2 == 0:
            evens_accum.append(src_nodes[pos])
        return collect_evens(src_nodes, evens_accum, pos + 1)

    evens_list: List[int] = collect_evens(nodes_collection, [], 0)

    if not evens_list:
        return []

    def find_min_val(array: List[int], current_min: int, idx: int) -> int:
        if idx == len(array):
            return current_min
        next_min = array[idx] if array[idx] < current_min else current_min
        return find_min_val(array, next_min, idx + 1)

    minimum_even: int = find_min_val(evens_list, evens_list[0], 1)

    def locate_index(arr: List[int], target: int, position: int) -> int:
        if position == len(arr):
            return -1
        if arr[position] == target:
            return position
        return locate_index(arr, target, position + 1)

    index_of_min: int = locate_index(nodes_collection, minimum_even, 0)

    return [minimum_even, index_of_min]