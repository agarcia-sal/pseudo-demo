from typing import List

def search(list_of_integers: List[int]) -> int:
    max_val: int = 0
    idx: int = 0
    length: int = len(list_of_integers)

    # Find the maximum value in the list
    while idx < length:
        current_element: int = list_of_integers[idx]
        if current_element > max_val:
            max_val = current_element
        idx += 1

    # Frequency array covering all values from 0 to max_val
    freq_arr: List[int] = [0] * (max_val + 1)

    pos: int = 0
    # Count frequency of each element
    while pos < length:
        elem: int = list_of_integers[pos]
        freq_arr[elem] += 1
        pos += 1

    result: int = -1
    counter: int = 1
    freq_len: int = len(freq_arr)

    # Find the largest integer where frequency >= integer value
    while counter < freq_len:
        count_value: int = freq_arr[counter]
        if count_value >= counter:
            result = counter
        counter += 1

    return result