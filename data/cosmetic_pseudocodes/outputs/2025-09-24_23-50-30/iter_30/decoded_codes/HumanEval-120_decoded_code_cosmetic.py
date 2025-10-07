from typing import List


def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    n = len(array_of_integers)
    # Perform insertion sort on the array
    for i in range(1, n):
        j = i
        while j > 0 and array_of_integers[j - 1] > array_of_integers[j]:
            array_of_integers[j], array_of_integers[j - 1] = array_of_integers[j - 1], array_of_integers[j]
            j -= 1
    slice_start = n - positive_integer_k
    res: List[int] = []
    i = slice_start
    while i < n:
        res.append(array_of_integers[i])
        i += 1
    return res