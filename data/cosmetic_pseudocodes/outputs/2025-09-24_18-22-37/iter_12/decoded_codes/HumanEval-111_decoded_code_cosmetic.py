from typing import Dict

def histogram(test_string_param: str) -> Dict[str, int]:
    frequency_map_var: Dict[str, int] = {}
    letters_array_var = test_string_param.split(" ")
    highest_frequency_var = 0

    idx_var = 0
    while idx_var < len(letters_array_var):
        current_letter_var = letters_array_var[idx_var]
        count_current_letter_var = 0
        for inner_idx_var in range(len(letters_array_var)):
            if letters_array_var[inner_idx_var] == current_letter_var and current_letter_var != "":
                count_current_letter_var += 1
        if count_current_letter_var > highest_frequency_var:
            highest_frequency_var = count_current_letter_var
        idx_var += 1

    if highest_frequency_var > 0:
        for letter_var in letters_array_var:
            found_count_var = 0
            pos_var = 0
            while pos_var < len(letters_array_var):
                if letters_array_var[pos_var] == letter_var and letter_var != "":
                    found_count_var += 1
                pos_var += 1
            if found_count_var == highest_frequency_var:
                frequency_map_var[letter_var] = highest_frequency_var

    return frequency_map_var