from typing import List, TypeVar, Sequence

T = TypeVar('T')

def sort_third(original_collection: Sequence[T]) -> List[T]:
    temp_storage: List[T] = list(original_collection)
    divisible_positions: List[int] = []
    reordered_elements: List[T] = []

    def gather_positions(current_index: int) -> None:
        if current_index >= len(temp_storage):
            return
        divisible_positions.append(current_index)
        gather_positions(current_index + 3)

    def extract_values(positions_list: List[int]) -> None:
        if not positions_list:
            return
        reordered_elements.append(temp_storage[positions_list[0]])
        extract_values(positions_list[1:])

    def place_sorted_values(sorted_list: List[T], positions_list: List[int], idx: int) -> None:
        if idx >= len(sorted_list):
            return
        temp_storage[positions_list[idx]] = sorted_list[idx]
        place_sorted_values(sorted_list, positions_list, idx + 1)

    gather_positions(0)
    extract_values(divisible_positions)
    reordered_elements.sort()
    place_sorted_values(reordered_elements, divisible_positions, 0)

    return temp_storage