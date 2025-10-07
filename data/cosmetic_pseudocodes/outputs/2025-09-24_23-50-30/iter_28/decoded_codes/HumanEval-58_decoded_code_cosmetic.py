from typing import List, Set, TypeVar

T = TypeVar('T')

def common(alpha: List[T], beta: List[T]) -> List[T]:
    def hashelement(hs: Set[T], val: T) -> Set[T]:
        if val not in hs:
            hs.add(val)
        return hs

    def recurse_outer(i: int, j: int, acc_h: Set[T]) -> Set[T]:
        if i >= len(alpha):
            return acc_h
        if j >= len(beta):
            return recurse_outer(i + 1, 0, acc_h)
        updated_acc_h = hashelement(acc_h, alpha[i]) if alpha[i] == beta[j] else acc_h
        return recurse_outer(i, j + 1, updated_acc_h)

    def to_sorted_array(hs: Set[T]) -> List[T]:
        arr = list(hs)
        n = len(arr)
        for x in range(n - 1):
            for y in range(x + 1, n):
                if arr[y] < arr[x]:
                    arr[x], arr[y] = arr[y], arr[x]
        return arr

    initial_hash: Set[T] = set()
    intersection_hash = recurse_outer(0, 0, initial_hash)
    return to_sorted_array(intersection_hash)