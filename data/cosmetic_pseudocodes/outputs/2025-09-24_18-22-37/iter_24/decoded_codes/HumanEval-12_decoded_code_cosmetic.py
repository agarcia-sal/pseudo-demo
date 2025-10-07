from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    result_string: Optional[str]
    max_len: int
    found_flag: bool
    idx: int

    found_flag = False
    idx = 0

    if not list_of_strings:
        result_string = None
        found_flag = True

    while idx < len(list_of_strings) and not found_flag:
        idx += 1

    if not found_flag:
        lengths_array: List[int] = []
        i = 0

        while i < len(list_of_strings):
            lengths_array.append(len(list_of_strings[i]))
            i += 1

        max_len = lengths_array[0]
        j = 1

        while j < len(lengths_array):
            if lengths_array[j] > max_len:
                max_len = lengths_array[j]
            j += 1

        idx = 0
        while idx < len(list_of_strings) and not found_flag:
            current_string = list_of_strings[idx]
            if len(current_string) == max_len:
                result_string = current_string
                found_flag = True
            idx += 1

    return result_string