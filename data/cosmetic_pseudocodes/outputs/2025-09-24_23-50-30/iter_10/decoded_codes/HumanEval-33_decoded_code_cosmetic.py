from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    # Copy input list
    list_out: List[T] = []
    index: int = 0
    while index < len(list_input):
        list_out.append(list_input[index])
        index += 1

    # Extract elements at indices divisible by 3
    extracted: List[T] = []
    curr: int = 0
    while curr < len(list_out):
        if curr % 3 == 0:
            extracted.append(list_out[curr])
        curr += 1

    # Sort extracted elements using selection sort
    sorted_segment: List[T] = []
    while len(extracted) > 0:
        min_val = extracted[0]
        index_min = 0
        pos = 1
        while pos < len(extracted):
            if extracted[pos] < min_val:
                min_val = extracted[pos]
                index_min = pos
            pos += 1
        sorted_segment.append(min_val)
        extracted.pop(index_min)

    # Replace original list_out elements at indices divisible by 3
    replace_counter = 0
    for k in range(len(list_out)):
        if k % 3 == 0:
            list_out[k] = sorted_segment[replace_counter]
            replace_counter += 1

    return list_out