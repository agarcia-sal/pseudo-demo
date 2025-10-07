from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    letters_list = test_string.split(' ')
    top_frequency = -1

    idx = 0
    while idx < len(letters_list):
        current_letter = letters_list[idx]
        if current_letter != "":
            current_count = 0
            scan_idx = 0
            while scan_idx < len(letters_list):
                if letters_list[scan_idx] == current_letter:
                    current_count += 1
                scan_idx += 1
            if current_count > top_frequency:
                top_frequency = current_count
        idx += 1

    if top_frequency > 0:
        processed_letters: Dict[str, bool] = {}
        for letter in letters_list:
            if letter != "" and letter not in processed_letters:
                letter_count = 0
                position = 0
                while position < len(letters_list):
                    if letters_list[position] == letter:
                        letter_count += 1
                    position += 1
                if letter_count == top_frequency:
                    freq_map[letter] = top_frequency
                processed_letters[letter] = True

    return freq_map