from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    first_seq: List[T] = []
    second_seq: List[T] = []
    len_total: int = len(list_of_elements)
    idx: int = 0
    while idx < len_total:
        if idx % 2 == 0:
            first_seq.append(list_of_elements[idx])
        else:
            second_seq.append(list_of_elements[idx])
        idx += 1
    first_seq.sort()
    merged_list: List[T] = []
    limit: int = len(second_seq)
    i: int = 0
    while i < limit:
        merged_list.append(first_seq[i])
        merged_list.append(second_seq[i])
        i += 1
    if len(first_seq) > len(second_seq):
        merged_list.append(first_seq[-1])
    return merged_list