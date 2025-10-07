from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    chars: list[str] = []
    idx = 1
    length = len(test_string)
    while idx <= length:
        ch = test_string[idx - 1]
        if ch == " ":
            chars.append("")
        else:
            if not chars:
                chars = [ch]
            else:
                chars[-1] += ch
        idx += 1

    top_count = 0
    pos = 1
    chars_len = len(chars)
    while pos <= chars_len:
        curr_char = chars[pos - 1]
        if curr_char != "":
            count_curr = 0
            scan = 1
            while scan <= chars_len:
                if chars[scan - 1] == curr_char:
                    count_curr += 1
                scan += 1
            if count_curr > top_count:
                top_count = count_curr
        pos += 1

    if top_count > 0:
        pos2 = 1
        while pos2 <= chars_len:
            curr_char2 = chars[pos2 - 1]
            if curr_char2 != "":
                tally = 0
                scan2 = 1
                while scan2 <= chars_len:
                    if chars[scan2 - 1] == curr_char2:
                        tally += 1
                    scan2 += 1
                if tally == top_count:
                    freq_map[curr_char2] = top_count
            pos2 += 1

    return freq_map