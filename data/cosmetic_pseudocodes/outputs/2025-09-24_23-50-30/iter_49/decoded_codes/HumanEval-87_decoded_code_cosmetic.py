from typing import List, Tuple, Callable


def get_row(matrix: List[List[int]], key: int) -> List[Tuple[int, int]]:
    def recur_outer(idx_outer: int, acc_outer: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if idx_outer > len(matrix) - 1:
            return acc_outer
        else:
            def recur_inner(idx_inner: int, acc_inner: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
                if idx_inner > len(matrix[idx_outer]) - 1:
                    return acc_inner
                else:
                    acc_inner2 = (acc_inner + [(idx_outer, idx_inner)]
                                  if matrix[idx_outer][idx_inner] == key else acc_inner)
                    return recur_inner(idx_inner + 1, acc_inner2)
            updated_acc = recur_inner(0, acc_outer)
            return recur_outer(idx_outer + 1, updated_acc)

    collected_coords: List[Tuple[int, int]] = recur_outer(0, [])

    def cmp_first_asc(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
        return a[0] > b[0]

    def cmp_second_desc(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
        return a[1] < b[1]

    temp_sorted = collected_coords
    n = len(temp_sorted)

    def sort_pass(arr: List[Tuple[int, int]], cmp_func: Callable[[Tuple[int, int], Tuple[int, int]], bool], i: int) -> List[Tuple[int, int]]:
        if i >= n:
            return arr
        else:
            def inner_sort(j: int, arr_inner: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
                if j >= n - 1:
                    return arr_inner
                else:
                    if cmp_func(arr_inner[j], arr_inner[j + 1]):
                        arr_inner[j], arr_inner[j + 1] = arr_inner[j + 1], arr_inner[j]
                    return inner_sort(j + 1, arr_inner)
            arr_after_pass = inner_sort(0, arr)
            return sort_pass(arr_after_pass, cmp_func, i + 1)

    first_sorted = sort_pass(temp_sorted, cmp_second_desc, 0)
    final_sorted = sort_pass(first_sorted, cmp_first_asc, 0)

    return final_sorted