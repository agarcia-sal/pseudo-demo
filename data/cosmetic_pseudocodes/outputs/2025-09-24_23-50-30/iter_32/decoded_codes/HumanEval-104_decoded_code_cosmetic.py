from typing import Iterable, List


def unique_digits(enumeration_of_positives: Iterable[int]) -> List[int]:
    accumulation: List[int] = []
    for candidate_var in enumeration_of_positives:
        is_odd_flag = True
        candidate_str = str(candidate_var)
        digit_index = 0
        while digit_index < len(candidate_str) and is_odd_flag:
            numeric_digit = int(candidate_str[digit_index])
            if numeric_digit % 2 == 0:
                is_odd_flag = False
            else:
                digit_index += 1
        if is_odd_flag:
            accumulation.append(candidate_var)

    sorted_accumulation: List[int] = []
    while accumulation:
        min_element = accumulation[0]
        position_var = 0
        scan_var = 1
        while scan_var < len(accumulation):
            if accumulation[scan_var] < min_element:
                min_element = accumulation[scan_var]
                position_var = scan_var
            scan_var += 1
        sorted_accumulation.append(min_element)
        del accumulation[position_var]

    return sorted_accumulation