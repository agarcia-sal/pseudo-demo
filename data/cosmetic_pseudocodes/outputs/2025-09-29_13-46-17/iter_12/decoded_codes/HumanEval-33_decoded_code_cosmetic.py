from typing import List, Tuple, Callable, TypeVar

T = TypeVar('T')


def sort_third(a: List[T]) -> List[T]:
    # Helper: foldi - fold with index over range [start, end]
    def foldi(
        f: Callable[[int, int, List[Tuple[int, T]]], List[Tuple[int, T]]],
        acc: List[Tuple[int, T]],
        start: int,
        end: int,
    ) -> List[Tuple[int, T]]:
        for i in range(start, end + 1):
            acc = f(i, i, acc)
        return acc

    # foldl - left fold
    def foldl(f: Callable[[T, T], T], acc: T, xs: List[T]) -> T:
        for x in xs:
            acc = f(acc, x)
        return acc

    # p⊃ - merge two sorted lists by first element of tuples, merges recursively
    def merge_sorted(
        xs: List[Tuple[int, T]], ys: List[Tuple[int, T]]
    ) -> List[Tuple[int, T]]:
        result = []
        i, j = 0, 0
        while i < len(xs) and j < len(ys):
            if xs[i][0] < ys[j][0]:
                result.append(xs[i])
                i += 1
            else:
                result.append(ys[j])
                j += 1
        result.extend(xs[i:])
        result.extend(ys[j:])
        return result

    # ✦ - merge sort variant on list of tuples
    def merge_sort(lst: List[Tuple[int, T]]) -> List[Tuple[int, T]]:
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge_sorted(left, right)

    # Build list of (index, a[index]) where index mod 3 == 0 using foldi
    tuples_mod3: List[Tuple[int, T]] = foldi(
        lambda idx, _, acc: acc + [(idx, a[idx])] if idx % 3 == 0 else acc,
        [],
        0,
        len(a) - 1,
    )

    # Extract values from tuples_mod3
    values = [t[1] for t in tuples_mod3]

    # Sort values with stable sort (using merge_sort on tuples keyed by value)
    # First create tuples: (index, value), sort by value using built-in stable sort is simpler
    # But to follow pseudocode, we sort keys after sorting by index

    # Sort tuples_mod3 by their value (second element) but keep pairs
    # We'll sort by value while preserving indices, then reorder indices accordingly

    # Prepare pairs (index, value)
    pairs = tuples_mod3.copy()
    # Sort pairs by value
    pairs_sorted_by_value = sorted(pairs, key=lambda x: x[1])

    # Extract just values sorted
    sorted_values = [p[1] for p in pairs_sorted_by_value]

    # Extract just indices to assign sorted values back
    indices = [p[0] for p in tuples_mod3]

    # Assign sorted values back to a at indices mod 3 == 0
    for idx, val in zip(indices, sorted_values):
        a[idx] = val

    return a