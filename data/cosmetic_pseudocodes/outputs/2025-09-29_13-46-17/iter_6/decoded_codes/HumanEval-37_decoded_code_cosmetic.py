from typing import List, Tuple, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    def SPLIT_ELEMENTS(inputList: List[T], idx: int, evens_acc: List[T], odds_acc: List[T]) -> Tuple[List[T], List[T]]:
        if idx >= LENGTH(inputList):
            return evens_acc, odds_acc
        else:
            if idx % 2 == 0:
                return SPLIT_ELEMENTS(inputList, idx + 1, APPEND_TO(evens_acc, inputList[idx]), odds_acc)
            else:
                return SPLIT_ELEMENTS(inputList, idx + 1, evens_acc, APPEND_TO(odds_acc, inputList[idx]))

    def GET_RESULT(iter: int, acc: List[T], tupleList: Tuple[List[T], List[T]]) -> List[T]:
        evenList, oddList = tupleList
        if iter >= MIN(LENGTH(evenList), LENGTH(oddList)):
            if LENGTH(evenList) > LENGTH(oddList):
                return CONCATENATE(acc, [evenList[LENGTH(evenList) - 1]])
            else:
                return acc
        else:
            return GET_RESULT(iter + 1, CONCATENATE(acc, [evenList[iter], oddList[iter]]), (evenList, oddList))

    def sort(arr: List[T]) -> List[T]:
        def RECURSIVE_SORT(arrayParam: List[T], pos: int) -> List[T]:
            if pos >= LENGTH(arrayParam):
                return arrayParam
            else:
                keyValue = arrayParam[pos]
                j = pos - 1

                def SHIFT_LEFT(arrayShft: List[T], idx: int, keyVal: T) -> List[T]:
                    if idx < 0 or arrayShft[idx] <= keyVal:
                        return arrayShft
                    else:
                        modifiedArray = INSERT_AT(arrayShft, idx + 1, arrayShft[idx])
                        shortenedArray = REMOVE_AT(modifiedArray, idx)
                        return SHIFT_LEFT(shortenedArray, idx - 1, keyVal)

                partiallySorted = SHIFT_LEFT(arrayParam, j, keyValue)
                insertedArray = UPDATE_AT(partiallySorted, j + 1, keyValue)
                return RECURSIVE_SORT(insertedArray, pos + 1)

        return RECURSIVE_SORT(arr, 1)

    def CONCATENATE(l1: List[T], l2: List[T]) -> List[T]:
        def FOLD_LEFT(lst2: List[T], acc: List[T], func) -> List[T]:
            for el in lst2:
                acc = func(acc, el)
            return acc
        return FOLD_LEFT(l2, l1, lambda acc, el: APPEND_TO(acc, el))

    def APPEND_TO(lst: List[T], element: T) -> List[T]:
        return lst + [element]

    def MIN(a: int, b: int) -> int:
        return a if a <= b else b

    def LENGTH(someList: List[T]) -> int:
        count = 0
        for _ in someList:
            count += 1
        return count

    def UPDATE_AT(lst: List[T], idx: int, val: T) -> List[T]:
        return SLICE(lst, 0, idx) + [val] + SLICE(lst, idx + 1, LENGTH(lst))

    def REMOVE_AT(lst: List[T], idx: int) -> List[T]:
        return SLICE(lst, 0, idx) + SLICE(lst, idx + 1, LENGTH(lst))

    def INSERT_AT(lst: List[T], idx: int, val: T) -> List[T]:
        return SLICE(lst, 0, idx) + [val] + SLICE(lst, idx, LENGTH(lst))

    def SLICE(lst: List[T], start: int, end: int) -> List[T]:
        res: List[T] = []
        i = start
        while i < end:
            res = APPEND_TO(res, lst[i])
            i += 1
        return res

    def GET_EVEN_INDICES(lst: List[T]) -> List[T]:
        def GET_EVEN_INDICES_HELPER(l: List[T], currIdx: int, acc: List[T]) -> List[T]:
            if currIdx >= LENGTH(l):
                return acc
            elif currIdx % 2 == 0:
                return GET_EVEN_INDICES_HELPER(l, currIdx + 1, APPEND_TO(acc, l[currIdx]))
            else:
                return GET_EVEN_INDICES_HELPER(l, currIdx + 1, acc)
        return GET_EVEN_INDICES_HELPER(lst, 0, [])

    def GET_ODD_INDICES(lst: List[T]) -> List[T]:
        def GET_ODD_INDICES_HELPER(l: List[T], currIdx: int, acc: List[T]) -> List[T]:
            if currIdx >= LENGTH(l):
                return acc
            elif currIdx % 2 != 0:
                return GET_ODD_INDICES_HELPER(l, currIdx + 1, APPEND_TO(acc, l[currIdx]))
            else:
                return GET_ODD_INDICES_HELPER(l, currIdx + 1, acc)
        return GET_ODD_INDICES_HELPER(lst, 0, [])

    even_indexed_elements = (lambda eList: 
        (lambda l: l if LENGTH(l) <= 1 else sort(l))
        (eList)
    )(GET_EVEN_INDICES(list_of_elements))

    odd_indexed_elements = GET_ODD_INDICES(list_of_elements)

    return GET_RESULT(0, [], (even_indexed_elements, odd_indexed_elements))