from typing import Dict

def histogram(input_text: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    char_sequence = input_text.split(" ")
    peak_frequency = 0

    idx = 0
    length = len(char_sequence)
    while idx < length:
        current_char = char_sequence[idx]
        occur_count = 0
        walk = 0
        while walk < length:
            if char_sequence[walk] == current_char:
                occur_count += 1
            walk += 1

        if occur_count > peak_frequency and current_char != "":
            peak_frequency = occur_count
        idx += 1

    if peak_frequency > 0:
        for element in char_sequence:
            temp_count = 0
            for candidate in char_sequence:
                if candidate == element:
                    temp_count += 1
            if temp_count == peak_frequency:
                freq_map[element] = peak_frequency

    return freq_map