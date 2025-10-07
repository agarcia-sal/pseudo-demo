from typing import Dict

def histogram(input_text: str) -> Dict[str, int]:
    frequency_map: Dict[str, int] = {}
    tokens: list[str] = []
    idx: int = 0
    while idx < len(input_text):
        current_char = input_text[idx]
        if current_char == ' ':
            tokens.append("")
        else:
            if not tokens:
                tokens.append(current_char)
            else:
                tokens[-1] += current_char
        idx += 1

    max_freq = 0
    pos = 0
    while pos < len(tokens):
        token = tokens[pos]
        count_occurrences = 0
        scan_pos = 0
        while scan_pos < len(tokens):
            if tokens[scan_pos] == token:
                count_occurrences += 1
            scan_pos += 1
        if count_occurrences > max_freq and token != "":
            max_freq = count_occurrences
        pos += 1

    if max_freq != 0:
        cursor = 0
        while cursor < len(tokens):
            char_item = tokens[cursor]
            count_repeats = 0
            scan_index = 0
            while scan_index < len(tokens):
                if tokens[scan_index] == char_item:
                    count_repeats += 1
                scan_index += 1
            if count_repeats == max_freq:
                frequency_map[char_item] = max_freq
            cursor += 1

    return frequency_map