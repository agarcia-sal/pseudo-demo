from typing import Dict


def histogram(test_string: str) -> Dict[str, int]:
    frequency_dictionary: Dict[str, int] = {}
    list_of_letters = test_string.split(" ")
    max_occurrence = -1

    i = 0
    while i < len(list_of_letters):
        current_letter = list_of_letters[i]
        if current_letter != "":
            count = 0
            j = 0
            while j < len(list_of_letters):
                if list_of_letters[j] == current_letter:
                    count += 1
                j += 1
            if count > max_occurrence:
                max_occurrence = count
        i += 1

    if max_occurrence > 0:
        idx = 0
        while idx < len(list_of_letters):
            current_letter = list_of_letters[idx]
            if current_letter != "":
                temp_count = 0
                k = 0
                while k < len(list_of_letters):
                    if list_of_letters[k] == current_letter:
                        temp_count += 1
                    k += 1
                if temp_count == max_occurrence:
                    frequency_dictionary[current_letter] = max_occurrence
            idx += 1

    return frequency_dictionary