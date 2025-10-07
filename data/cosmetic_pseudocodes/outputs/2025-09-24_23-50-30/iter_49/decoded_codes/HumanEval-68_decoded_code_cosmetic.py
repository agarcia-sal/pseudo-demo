from typing import List, Tuple

def pluck(assoc_nodes: List[int]) -> List[int]:
    def recursive_filter(seq_nodes: List[int], acc_filtered: List[int]) -> List[int]:
        if not seq_nodes:
            return acc_filtered
        head_node, *tail_nodes = seq_nodes
        if head_node % 2 == 0:
            return recursive_filter(tail_nodes, acc_filtered + [head_node])
        return recursive_filter(tail_nodes, acc_filtered)

    def recursive_min_search(values_list: List[int], best_val: int, best_idx: int, curr_idx: int) -> Tuple[int, int]:
        if curr_idx == len(values_list):
            return best_val, best_idx
        current_val = values_list[curr_idx]
        if current_val < best_val:
            return recursive_min_search(values_list, current_val, curr_idx, curr_idx + 1)
        return recursive_min_search(values_list, best_val, best_idx, curr_idx + 1)

    if len(assoc_nodes) == 0:
        return []

    filtered_evens = recursive_filter(assoc_nodes, [])
    if not filtered_evens:
        return []

    first_even = filtered_evens[0]
    start_idx = 0
    min_even, min_index_in_evens = recursive_min_search(filtered_evens, first_even, start_idx, start_idx + 1)

    def locate_in_original(sequence: List[int], target: int, scan: int) -> int:
        if scan == len(sequence):
            return -1
        if sequence[scan] == target:
            return scan
        return locate_in_original(sequence, target, scan + 1)

    final_index = locate_in_original(assoc_nodes, min_even, 0)
    return [min_even, final_index]