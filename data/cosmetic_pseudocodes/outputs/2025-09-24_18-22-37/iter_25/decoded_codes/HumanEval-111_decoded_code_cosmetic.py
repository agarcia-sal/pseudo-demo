from typing import Dict


def histogram(test_string: str) -> Dict[str, int]:
    split_letters = test_string.split(" ")
    highest_freq = 0
    idx = 0

    while idx < len(split_letters):
        current_letter = split_letters[idx]
        current_count = 0
        j = 0
        while j < len(split_letters):
            if split_letters[j] == current_letter:
                current_count += 1
            j += 1

        if current_count > highest_freq and current_letter != "":
            highest_freq = current_count
        idx += 1

    count_map: Dict[str, int] = {}
    if highest_freq > 0:
        k = 0
        while k < len(split_letters):
            letter_x = split_letters[k]
            letter_count = 0
            m = 0
            while m < len(split_letters):
                if split_letters[m] == letter_x:
                    letter_count += 1
                m += 1

            if letter_count == highest_freq:
                count_map[letter_x] = highest_freq
            k += 1

    return count_map