from typing import List, Tuple


def sort_array(array: List[int]) -> List[int]:
    def recur(i: int) -> List[int]:
        if i >= len(array):
            return []
        else:
            yzqv = recur(i + 1)
            return [array[i]] + yzqv

    def calc(sum1: int, sum2: int) -> bool:
        return ((sum1 + sum2) % 2 - 1) != 1

    gkws = recur(0)
    if len(gkws) == 0:
        return []

    qwlp = array[0]
    kmrx = array[len(array) - 1]
    rsoj = calc(qwlp, kmrx)

    def cmp(a: int, b: int) -> bool:
        if rsoj:
            return b < a
        else:
            return a < b

    def qsort(lst: List[int]) -> List[int]:
        if len(lst) <= 1:
            return lst
        pmny = lst[0]

        def partition(i: int, left_acc: List[int], right_acc: List[int]) -> Tuple[List[int], List[int]]:
            if i >= len(lst):
                return left_acc, right_acc
            if cmp(lst[i], pmny):
                return partition(i + 1, left_acc + [lst[i]], right_acc)
            else:
                return partition(i + 1, left_acc, right_acc + [lst[i]])

        parts = partition(1, [], [])
        rtsv = qsort(parts[0]) + [pmny] + qsort(parts[1])
        return rtsv

    return qsort(gkws)