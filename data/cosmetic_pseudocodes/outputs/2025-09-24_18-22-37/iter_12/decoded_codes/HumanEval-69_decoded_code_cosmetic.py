from typing import List

def search(numbers: List[int]) -> int:
    temp_max: int = 0
    idx: int = 0
    while idx < len(numbers):
        if numbers[idx] > temp_max:
            temp_max = numbers[idx]
        idx += 1

    freq_arr: List[int] = [0] * (temp_max + 1)
    pos: int = 0
    while pos < len(numbers):
        val: int = numbers[pos]
        old_count: int = freq_arr[val]
        freq_arr[val] = old_count + 1
        pos += 1

    result: int = -1
    for counter in range(len(freq_arr) - 1, 0, -1):
        if freq_arr[counter] >= counter:
            result = counter
            break

    return result