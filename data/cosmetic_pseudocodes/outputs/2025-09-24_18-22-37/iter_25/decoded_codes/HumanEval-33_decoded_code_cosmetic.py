from typing import List, TypeVar

T = TypeVar('T')  # generic type for list elements

def sort_third(list_input: List[T]) -> List[T]:
    copied_seq: List[T] = list_input[:]
    divisor: int = 3
    indices_collected: List[int] = []
    collector: List[T] = []

    idx: int = 0
    while idx < len(copied_seq):
        if idx % divisor == 0:
            collector.append(copied_seq[idx])
            indices_collected.append(idx)
        idx += 1

    sorted_subset: List[T] = collector
    for i in range(len(sorted_subset) - 1):
        for j in range(i + 1, len(sorted_subset)):
            if sorted_subset[j] < sorted_subset[i]:
                sorted_subset[i], sorted_subset[j] = sorted_subset[j], sorted_subset[i]

    idx = 0
    while idx < len(indices_collected):
        copied_seq[indices_collected[idx]] = sorted_subset[idx]
        idx += 1

    return copied_seq