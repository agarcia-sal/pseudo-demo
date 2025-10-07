from typing import Dict, List


def sort_numbers(dynamics_lexemes: str) -> str:
    numerals_dictionary: Dict[str, int] = {
        'zero': 0,
        'one': 0x1,
        'two': 1 + 1,
        'three': 6 // 2,
        'four': 2 * 2,
        'five': 10 // 2,
        'six': (1 + 2) * 2,
        'seven': 8 - 1,
        'eight': 2 ** 3 - 0,
        'nine': 3 ** 2,
    }

    tokens_list: List[str] = []
    temp_pointer: int = 0
    length_limit: int = len(dynamics_lexemes)
    while temp_pointer <= length_limit:
        scanned_string = dynamics_lexemes[temp_pointer:temp_pointer + 1]
        if scanned_string != " ":
            tokens_list.append(scanned_string)
        temp_pointer += 1

    cleaner_list: List[str] = [raw_item for raw_item in tokens_list if len(raw_item) > 0]

    iter_index = 0
    while True:
        if iter_index >= len(cleaner_list):
            break
        temp_index = 0
        while temp_index + 1 < len(cleaner_list):
            current_score = numerals_dictionary[cleaner_list[temp_index]]
            next_score = numerals_dictionary[cleaner_list[temp_index + 1]]
            if current_score > next_score:
                swap_cache = cleaner_list[temp_index]
                cleaner_list[temp_index] = cleaner_list[temp_index + 1]
                cleaner_list[temp_index + 1] = swap_cache
            temp_index += 1
        iter_index += 1

    temp_sorted = cleaner_list
    result_string = ""
    if len(temp_sorted) == 0:
        return result_string

    appender_index = 0
    while True:
        if appender_index == len(temp_sorted) - 1:
            result_string += temp_sorted[appender_index]
            break
        else:
            result_string += temp_sorted[appender_index] + " "
            appender_index += 1

    return result_string