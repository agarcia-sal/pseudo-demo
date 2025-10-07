from typing import List, TypeVar

T = TypeVar('T')


def sort_third(list_input: List[T]) -> List[T]:
    working_list: List[T] = list_input.copy()
    extracted_subset: List[T] = []

    idx: int = 0
    while idx < len(working_list):
        if idx % 3 == 0:
            extracted_subset.append(working_list[idx])
        idx += 1

    arranged_subset: List[T] = sorted(extracted_subset)

    replace_index: int = 0
    subset_index: int = 0
    while replace_index < len(working_list):
        if replace_index % 3 == 0:
            working_list[replace_index] = arranged_subset[subset_index]
            subset_index += 1
        replace_index += 1

    return working_list