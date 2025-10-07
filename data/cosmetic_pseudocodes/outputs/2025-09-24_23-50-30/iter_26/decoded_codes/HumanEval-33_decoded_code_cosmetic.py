from typing import Sequence, List, TypeVar

T = TypeVar('T')

def sort_third(sequence_param: Sequence[T]) -> List[T]:
    temp_seq: List[T] = list(sequence_param)

    def gather_values(position: int, collected: List[T]) -> List[T]:
        if position >= len(temp_seq):
            return collected
        return gather_values(position + 3, collected + [temp_seq[position]])

    index_filtered_values: List[T] = gather_values(0, [])
    sorted_filtered_values: List[T] = sorted(index_filtered_values)

    def substitute_values(position: int, idx: int, data: List[T]) -> List[T]:
        if position >= len(temp_seq):
            return data
        updated_data = data[:]
        updated_data[position] = sorted_filtered_values[idx]
        return substitute_values(position + 3, idx + 1, updated_data)

    temp_seq = substitute_values(0, 0, temp_seq)
    return temp_seq