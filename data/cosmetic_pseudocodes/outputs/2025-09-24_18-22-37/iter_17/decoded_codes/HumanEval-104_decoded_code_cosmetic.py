from typing import List


def unique_digits(sequence_of_nat_nums: List[int]) -> List[int]:
    collected_odds: List[int] = []
    idx: int = 0

    while idx < len(sequence_of_nat_nums):
        curr_val = sequence_of_nat_nums[idx]
        digit_list: List[int] = []
        temp_num = curr_val

        while temp_num > 0:
            rem = temp_num % 10
            digit_list.append(rem)
            temp_num = (temp_num - rem) // 10  # integer division

        all_odd = True
        cursor = 0
        while cursor < len(digit_list) and all_odd:
            if digit_list[cursor] % 2 == 0:
                all_odd = False
            cursor += 1

        if all_odd:
            collected_odds.append(curr_val)
        idx += 1

    sorted_vals: List[int] = []
    unsorted_vals = collected_odds

    while len(unsorted_vals) > 0:
        lowest = unsorted_vals[0]
        scan_index = 1
        while scan_index < len(unsorted_vals):
            if unsorted_vals[scan_index] < lowest:
                lowest = unsorted_vals[scan_index]
            scan_index += 1

        sorted_vals.append(lowest)

        filtered: List[int] = []
        pos = 0
        while pos < len(unsorted_vals):
            if unsorted_vals[pos] != lowest:
                filtered.append(unsorted_vals[pos])
            pos += 1
        unsorted_vals = filtered

    return sorted_vals