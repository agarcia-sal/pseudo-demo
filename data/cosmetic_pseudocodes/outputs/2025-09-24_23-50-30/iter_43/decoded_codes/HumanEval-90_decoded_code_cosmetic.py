from typing import List, Optional, Tuple


def next_smallest(arr_data: List[int]) -> Optional[int]:
    arr_temp: List[int] = []
    for i_idx in range(len(arr_data)):
        if arr_data[i_idx] not in arr_temp:
            arr_temp.append(arr_data[i_idx])
    quicksort_iterative(arr_temp)
    if len(arr_temp) < 2:
        return None
    else:
        return arr_temp[1]


def quicksort_iterative(lst_work: List[int]) -> None:
    stack_work: List[Tuple[int, int]] = []
    stack_work.append((0, len(lst_work) - 1))
    while stack_work:
        start_idx, end_idx = stack_work.pop()
        if start_idx < end_idx:
            pivot_idx = partition(lst_work, start_idx, end_idx)
            stack_work.append((start_idx, pivot_idx - 1))
            stack_work.append((pivot_idx + 1, end_idx))


def partition(lst_part: List[int], left_idx: int, right_idx: int) -> int:
    pivot_val = lst_part[right_idx]
    i_cursor = left_idx - 1
    for j_cursor in range(left_idx, right_idx):
        if lst_part[j_cursor] <= pivot_val:
            i_cursor += 1
            lst_part[i_cursor], lst_part[j_cursor] = lst_part[j_cursor], lst_part[i_cursor]
    lst_part[i_cursor + 1], lst_part[right_idx] = lst_part[right_idx], lst_part[i_cursor + 1]
    return i_cursor + 1