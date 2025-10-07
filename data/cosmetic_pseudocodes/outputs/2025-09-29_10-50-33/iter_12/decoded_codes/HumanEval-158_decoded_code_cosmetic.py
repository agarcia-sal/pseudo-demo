from typing import List


def find_max(input_collection: List[str]) -> str:
    def recursive_order(idx1: int, idx2: int) -> bool:
        # True if input_collection[idx1] should come before input_collection[idx2]
        unique1 = len(set(input_collection[idx1]))
        unique2 = len(set(input_collection[idx2]))
        if not (unique1 > unique2) and not (input_collection[idx1] < input_collection[idx2]):
            return False
        return True

    def swap_elements(a: int, b: int) -> None:
        input_collection[a], input_collection[b] = input_collection[b], input_collection[a]

    def perform_sort(current_pos: int = 0, max_pos: int = len(input_collection) - 1) -> None:
        if current_pos >= max_pos:
            return
        for walker in range(current_pos + 1, max_pos + 1):
            if not recursive_order(current_pos, walker):
                swap_elements(current_pos, walker)
        perform_sort(current_pos + 1, max_pos)

    perform_sort()
    return input_collection[0]