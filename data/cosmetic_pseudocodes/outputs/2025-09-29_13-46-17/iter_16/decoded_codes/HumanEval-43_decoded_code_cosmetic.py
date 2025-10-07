from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    n: int = len(list_of_integers)
    array: List[int] = list_of_integers

    def checker(i: int, arr: List[int]) -> bool:
        j: int = i + 1
        found: bool = False
        while j < n:
            s: int = arr[i] + arr[j]
            if s == 0:
                found = True
                return found
            j += 1
        return found

    i: int = 0
    result: bool = False
    while i < n and not result:
        result = checker(i, array)
        i += 1
    return result