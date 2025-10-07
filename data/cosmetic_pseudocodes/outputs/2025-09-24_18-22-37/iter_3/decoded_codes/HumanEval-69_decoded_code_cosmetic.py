from typing import List

def search(list_of_integers: List[int]) -> int:
    max_val: int = 0
    for val in list_of_integers:
        if val > max_val:
            max_val = val

    freq_arr: List[int] = [0] * (max_val + 1)
    pos: int = 0
    while pos < len(list_of_integers):
        current_val = list_of_integers[pos]
        freq_arr[current_val] += 1
        pos += 1

    result: int = -1

    def checkIndex(i: int) -> None:
        nonlocal result
        if i > max_val:
            return
        if freq_arr[i] >= i:
            result = i
        checkIndex(i + 1)

    checkIndex(1)
    return result