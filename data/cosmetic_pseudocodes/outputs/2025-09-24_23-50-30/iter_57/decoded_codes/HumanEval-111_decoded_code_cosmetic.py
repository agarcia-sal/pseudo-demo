from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    chars_list = test_string.split(" ")
    top_freq = 0
    # First pass: find the highest frequency of any non-empty string token
    for idx in range(len(chars_list)):
        current_char = chars_list[idx]
        char_count = 0
        scan_idx = 0
        while scan_idx < len(chars_list):
            if chars_list[scan_idx] == current_char:
                char_count += 1
            scan_idx += 1
        if char_count > 0 and current_char != "":
            if char_count > top_freq:
                top_freq = char_count

    freq_map: Dict[str, int] = {}
    if top_freq > 0:
        # Second pass: collect all strings with frequency equal to top_freq
        for pos in range(len(chars_list)):
            candidate_char = chars_list[pos]
            frequency_count = 0
            iter_pos = 0
            while iter_pos < len(chars_list):
                if chars_list[iter_pos] == candidate_char:
                    frequency_count += 1
                iter_pos += 1
            if frequency_count == top_freq:
                freq_map[candidate_char] = top_freq

    return freq_map