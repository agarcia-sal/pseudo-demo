from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    jump_elements: List[T] = []
    skip_elements: List[T] = []
    idx_jumping = 0
    idx_skipping = 1

    # Collect elements at even indices
    while idx_jumping < len(list_of_elements):
        jump_elements.append(list_of_elements[idx_jumping])
        idx_jumping += 2

    # Collect elements at odd indices
    while idx_skipping < len(list_of_elements):
        skip_elements.append(list_of_elements[idx_skipping])
        idx_skipping += 2

    jump_elements.sort()

    merged_output: List[T] = []
    idx_pair = 0

    # Interleave sorted even-index elements with odd-index elements
    while idx_pair < len(skip_elements):
        merged_output.append(jump_elements[idx_pair])
        merged_output.append(skip_elements[idx_pair])
        idx_pair += 1

    # Append last even-index element if present
    if len(jump_elements) > len(skip_elements):
        merged_output.append(jump_elements[-1])

    return merged_output