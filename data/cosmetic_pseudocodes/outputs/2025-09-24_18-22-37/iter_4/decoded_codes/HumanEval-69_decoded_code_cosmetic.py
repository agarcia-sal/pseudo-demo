from typing import List

def search(list_of_integers: List[int]) -> int:
    max_val: int = 0
    iterator: int = 0
    while iterator < len(list_of_integers):
        if list_of_integers[iterator] > max_val:
            max_val = list_of_integers[iterator]
        iterator += 1

    freq_array: List[int] = [0] * (max_val + 1)
    idx: int = 0
    while idx < len(list_of_integers):
        current_num: int = list_of_integers[idx]
        freq_array[current_num] += 1
        idx += 1

    resulting_value: int = -1
    check_index: int = 1
    while check_index <= len(freq_array) - 1:
        if freq_array[check_index] >= check_index:
            resulting_value = check_index
        check_index += 1

    return resulting_value