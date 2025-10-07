from typing import List, TypedDict


def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    IntList = List[int]

    class IterState(TypedDict):
        data: IntList
        pos: int

    def slice_from_end(s: IntList, count: int) -> IntList:
        def inner_slice(state: IterState, acc: IntList) -> IntList:
            if state['pos'] < len(state['data']) - count:
                return inner_slice({'data': state['data'], 'pos': state['pos'] + 1}, acc)
            else:
                if state['pos'] >= len(state['data']):
                    return acc[::-1]
                else:
                    return inner_slice({'data': state['data'], 'pos': state['pos'] + 1}, [state['data'][state['pos']]] + acc)
        return inner_slice({'data': s, 'pos': 0}, [])

    def quicksort(l: IntList) -> IntList:
        if not l:
            return []
        pivot = l[0]

        def filter_less(elems: IntList, pivotVal: int) -> IntList:
            if not elems:
                return []
            if elems[0] < pivotVal:
                return [elems[0]] + filter_less(elems[1:], pivotVal)
            else:
                return filter_less(elems[1:], pivotVal)

        def filter_greater_equal(elems: IntList, pivotVal: int) -> IntList:
            if not elems:
                return []
            if elems[0] >= pivotVal:
                return [elems[0]] + filter_greater_equal(elems[1:], pivotVal)
            else:
                return filter_greater_equal(elems[1:], pivotVal)

        left_part = quicksort(filter_less(l[1:], pivot))
        right_part = quicksort(filter_greater_equal(l[1:], pivot))
        return left_part + [pivot] + right_part

    def identity_or_empty(kVal: int, arr: IntList) -> IntList:
        if not (kVal > 0):
            return []
        sorted_arr = quicksort(arr)
        return slice_from_end(sorted_arr, kVal)

    return identity_or_empty(positive_integer_k, array_of_integers)