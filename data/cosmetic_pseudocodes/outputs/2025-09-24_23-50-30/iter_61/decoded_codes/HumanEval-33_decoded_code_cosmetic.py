from typing import Sequence, List, Callable, TypeVar

T = TypeVar('T')

def sort_third(orig_seq: Sequence[T]) -> List[T]:
    temp_seq: List[T] = []
    filtered_vals: List[T] = []
    pos: int = 0  # declared but unused, kept for fidelity

    def copy_seq(idx: int) -> None:
        if idx >= len(orig_seq):
            return
        else:
            temp_seq.append(orig_seq[idx])
            copy_seq(idx + 1)

    copy_seq(0)

    index_list: List[int] = [k for k in range(len(temp_seq)) if (k % 3) == 0]

    m = 0
    while m < len(index_list):
        filtered_vals.append(temp_seq[index_list[m]])
        m += 1

    cmp_func: Callable[[T, T], bool] = lambda a, b: a <= b

    def insertion_sort(arr: List[T], n: int) -> None:
        p = 1
        while p < n:
            key = arr[p]
            q = p - 1
            while q >= 0 and not cmp_func(arr[q], key):
                arr[q + 1] = arr[q]
                q -= 1
            arr[q + 1] = key
            p += 1

    insertion_sort(filtered_vals, len(filtered_vals))

    w = 0
    length_index_list = len(index_list)
    while True:
        if w == length_index_list:
            break
        temp_seq[index_list[w]] = filtered_vals[w]
        w += 1

    return temp_seq