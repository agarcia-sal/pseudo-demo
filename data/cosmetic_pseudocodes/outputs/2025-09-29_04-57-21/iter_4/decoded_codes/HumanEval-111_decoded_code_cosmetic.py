from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    frequency_map: Dict[str, int] = {}
    letters_sequence = test_string.split(' ')
    peak_frequency = -1

    idx = 0
    length = len(letters_sequence)
    while idx < length:
        current_char = letters_sequence[idx]
        if current_char != "":
            occurrence = 0
            scan_index = 0
            while scan_index < length:
                if letters_sequence[scan_index] == current_char:
                    occurrence += 1
                scan_index += 1
            if occurrence > peak_frequency:
                peak_frequency = occurrence
        idx += 1

    if peak_frequency > 0:
        position = 0
        while position < length:
            candidate = letters_sequence[position]
            if candidate != "":
                count_check = 0
                iterator_pos = 0
                while iterator_pos < length:
                    if letters_sequence[iterator_pos] == candidate:
                        count_check += 1
                    iterator_pos += 1
                if count_check == peak_frequency:
                    frequency_map[candidate] = peak_frequency
            position += 1

    return frequency_map