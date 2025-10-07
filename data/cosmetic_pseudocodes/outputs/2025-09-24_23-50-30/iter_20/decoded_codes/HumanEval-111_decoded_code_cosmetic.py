from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    dict_result: Dict[str, int] = {}
    letters_arr = test_string.split(" ")
    max_val = 0
    idx = 0

    while idx < len(letters_arr):
        current_letter = letters_arr[idx]
        if current_letter != "":
            curr_count = 0
            inner_idx = 0
            while inner_idx < len(letters_arr):
                if letters_arr[inner_idx] == current_letter:
                    curr_count += 1
                inner_idx += 1
            if curr_count > max_val:
                max_val = curr_count
        idx += 1

    if max_val <= 0:
        return dict_result

    out_idx = 0
    while out_idx < len(letters_arr):
        letter_candidate = letters_arr[out_idx]
        count_candidate = 0
        count_idx = 0
        while count_idx < len(letters_arr):
            if letters_arr[count_idx] == letter_candidate:
                count_candidate += 1
            count_idx += 1
        if count_candidate == max_val:
            dict_result[letter_candidate] = max_val
        out_idx += 1

    return dict_result