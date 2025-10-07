from typing import List

def sort_even(arg1: List[int]) -> List[int]:
    arg2: List[int] = []
    arg3: List[int] = []
    for arg4 in range(len(arg1)):
        if arg4 % 2 == 0:
            arg2.append(arg1[arg4])
        else:
            arg3.append(arg1[arg4])
    arg5: int = len(arg2)
    arg6: int = len(arg3)
    arg7: int = arg5 - 1

    def arg8(arr: List[int], low: int, high: int) -> None:
        while low < high:
            pivot = arr[(low + high) // 2]
            i, j = low, high
            while True:
                while arr[i] < pivot:
                    i += 1
                while not (arr[j] < pivot):
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
                if i > j:
                    break
            if low < j:
                high = j
            else:
                low = i

    arg8(arg2, 0, arg7)

    arg9: List[int] = []

    def arg10(listA: List[int], listB: List[int], index: int, lengthA: int, lengthB: int) -> None:
        if index == lengthB:
            return
        arg9.append(listA[index])
        arg9.append(listB[index])
        arg10(listA, listB, index + 1, lengthA, lengthB)

    arg10(arg2, arg3, 0, arg5, arg6)

    if not (arg5 <= arg6):
        arg9.append(arg2[arg7])

    return arg9