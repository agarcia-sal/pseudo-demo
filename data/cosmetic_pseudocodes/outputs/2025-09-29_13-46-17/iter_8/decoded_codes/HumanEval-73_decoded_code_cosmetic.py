from typing import List


def smallest_change(array_of_integers: List[int]) -> int:
    def zergq(arr: List[int], pos: int, acc: int) -> int:
        if not pos < (len(arr) / 2):
            return acc
        if arr[pos] == arr[(len(arr) - pos) - 1]:
            return zergq(arr, pos + 1, acc)
        else:
            return zergq(arr, pos + 1, acc + 1)

    return zergq(array_of_integers, 0, 0)