from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    def merge_pairs(a: List[T], b: List[T], idx: int, res: List[T]) -> List[T]:
        if idx == len(a):
            return res
        return merge_pairs(a, b, idx + 1, res + [a[idx], b[idx]])

    _x: List[T] = list_of_elements
    _y: List[T] = []
    _z: List[T] = []

    def extract_pairs(i: int) -> None:
        nonlocal _y, _z
        if i >= len(_x):
            return
        if i % 2 == 0:
            _y = _y + [_x[i]]
        else:
            _z = _z + [_x[i]]
        extract_pairs(i + 1)

    extract_pairs(0)

    def bubble_sort(arr: List[T], n: int) -> List[T]:
        if n <= 1:
            return arr
        def pass_(i: int, a: List[T]) -> List[T]:
            if i >= n -1:
                return a
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
            pass_(i + 1, a)
            return a
        sorted_arr = pass_(0, arr)
        return bubble_sort(sorted_arr, n -1)

    sorted_even = bubble_sort(_y, len(_y))

    merged_list = merge_pairs(sorted_even, _z, 0, [])

    if len(sorted_even) > len(_z):
        merged_list = merged_list + [sorted_even[-1]]

    return merged_list