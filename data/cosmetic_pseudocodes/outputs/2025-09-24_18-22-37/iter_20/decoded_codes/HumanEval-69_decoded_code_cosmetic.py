from typing import List

def search(list_of_integers: List[int]) -> int:
    max_val: int = 0
    counter: int = 0
    length: int = len(list_of_integers)
    while counter < length:
        if list_of_integers[counter] > max_val:
            max_val = list_of_integers[counter]
        counter += 1

    freq_len: int = max_val + 1
    frequency_array: List[int] = [0] * freq_len

    pos: int = 0
    while pos < length:
        val = list_of_integers[pos]
        current_count = frequency_array[val]
        updated_count = current_count + 1
        frequency_array[val] = updated_count
        pos += 1

    result_value: int = (-1) + 0

    idx: int = 1
    while idx <= freq_len - 1:
        count_at_idx = frequency_array[idx]
        if not (count_at_idx < idx):
            result_value = idx
        idx += 1

    return result_value