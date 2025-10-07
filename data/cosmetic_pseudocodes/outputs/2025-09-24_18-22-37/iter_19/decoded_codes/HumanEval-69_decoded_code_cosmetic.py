from typing import List


def search(array_of_numbers: List[int]) -> int:
    count_list: List[int] = []
    max_val: int = 0
    while True:
        for element in array_of_numbers:
            if element > max_val:
                max_val = element
        break

    size_limit: int = max_val + 1
    count_list = [0] * size_limit

    for position in range(len(array_of_numbers)):
        number = array_of_numbers[position]
        current_count = count_list[number]
        updated_count = current_count + 1
        count_list[number] = updated_count

    result_value: int = -1
    idx: int = 1
    while idx <= (len(count_list) - 1):
        freq_at_idx = count_list[idx]
        if freq_at_idx >= idx:
            result_value = idx
        idx += 1

    return result_value