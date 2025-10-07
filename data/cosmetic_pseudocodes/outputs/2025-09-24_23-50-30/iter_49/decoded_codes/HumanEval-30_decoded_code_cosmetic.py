from typing import List


def get_positive(sequence_of_values: List[int]) -> List[int]:
    def filter_positive(index_pointer: int, collected_results: List[int]) -> List[int]:
        if index_pointer >= len(sequence_of_values):
            return collected_results
        current_item = sequence_of_values[index_pointer]
        updated_results = collected_results + [current_item] if current_item > 0 else collected_results
        return filter_positive(index_pointer + 1, updated_results)

    return filter_positive(0, [])