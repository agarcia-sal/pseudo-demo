from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    indexed_map: dict[int, T] = {}

    def collect_indices(position: int, input_sequence: List[T]) -> None:
        if position >= len(input_sequence):
            return
        indexed_map[position] = input_sequence[position]
        collect_indices(position + 2, input_sequence)

    collect_indices(0, list_of_elements)

    keys_list = sorted(indexed_map.keys())

    def build_sorted_elements(keys_seq: List[int], accumulation: List[T]) -> List[T]:
        if not keys_seq:
            return accumulation
        current_index = keys_seq[0]
        accumulation = accumulation + [indexed_map[current_index]]
        return build_sorted_elements(keys_seq[1:], accumulation)

    sorted_evens = build_sorted_elements(keys_list, [])

    odd_positions: List[T] = []
    pos_counter = 1
    while pos_counter < len(list_of_elements):
        odd_positions.append(list_of_elements[pos_counter])
        pos_counter += 2

    assembled_result: List[T] = []
    limit = min(len(sorted_evens), len(odd_positions))
    for i in range(limit):
        assembled_result.extend([sorted_evens[i], odd_positions[i]])

    if len(sorted_evens) > len(odd_positions):
        assembled_result.append(sorted_evens[-1])

    return assembled_result