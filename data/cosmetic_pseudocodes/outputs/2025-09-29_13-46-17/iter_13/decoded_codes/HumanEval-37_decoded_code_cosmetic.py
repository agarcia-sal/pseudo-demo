from typing import List, TypeVar

T = TypeVar('T')


def sort_even(list_of_elements: List[T]) -> List[T]:
    def extract(lst: List[T], idx: int, result: List[T]) -> List[T]:
        if idx >= len(lst):
            return result
        return extract(lst, idx + 2, result + [lst[idx]])

    def recur_merge(pair_A: List[T], pair_B: List[T], accum: List[T]) -> List[T]:
        if not pair_A and not pair_B:
            return accum
        if pair_A and pair_B:
            head_A, tail_A = pair_A[0], pair_A[1:]
            head_B, tail_B = pair_B[0], pair_B[1:]
            return recur_merge(tail_A, tail_B, accum + [head_A, head_B])
        if pair_A and not pair_B:
            return accum + pair_A
        # if pair_B and not pair_A: (not covered explicitly in pseudocode; safe to ignore per logic)
        return accum

    def sort_and_merge(A: List[T], B: List[T]) -> List[T]:
        def rec_sort(arr: List[T]) -> List[T]:
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = rec_sort(arr[:mid])
            right = rec_sort(arr[mid:])

            def merge(x: List[T], y: List[T], acc: List[T]) -> List[T]:
                if not x:
                    return acc + y
                if not y:
                    return acc + x
                if x[0] <= y[0]:
                    return merge(x[1:], y, acc + [x[0]])
                else:
                    return merge(x, y[1:], acc + [y[0]])

            return merge(left, right, [])

        sorted_A = rec_sort(A)
        return recur_merge(sorted_A, B, [])

    evens = extract(list_of_elements, 0, [])
    odds = extract(list_of_elements, 1, [])
    merged = recur_merge(evens, odds, [])
    return sort_and_merge(evens, odds)