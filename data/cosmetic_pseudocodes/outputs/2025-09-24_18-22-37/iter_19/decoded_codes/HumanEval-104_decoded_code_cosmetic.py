from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    collected_odds: List[int] = []
    idx: int = 0
    while idx < len(list_of_positive_integers):
        current_candidate: int = list_of_positive_integers[idx]
        is_all_odd: bool = True
        digit_string: str = str(current_candidate)
        pos: int = 0
        while pos < len(digit_string):
            if (int(digit_string[pos]) % 2) != 1:
                is_all_odd = False
            pos += 1
        if is_all_odd:
            collected_odds.append(current_candidate)
        idx += 1

    sorted_result: List[int] = []
    temp_list: List[int] = collected_odds.copy()
    while temp_list:
        min_val: int = temp_list[0]
        search_index: int = 1
        while search_index < len(temp_list):
            if temp_list[search_index] < min_val:
                min_val = temp_list[search_index]
            search_index += 1
        sorted_result.append(min_val)
        remove_index: int = 0
        while True:
            if temp_list[remove_index] == min_val:
                temp_list.pop(remove_index)
                break
            remove_index += 1

    return sorted_result