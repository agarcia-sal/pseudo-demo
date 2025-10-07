def how_many_times(original_string: str, target_substring: str) -> int:
    tally = 0
    pos = 0
    max_pos = len(original_string) - len(target_substring)
    while pos <= max_pos:
        if original_string[pos : pos + len(target_substring)] == target_substring:
            tally += 1
        pos += 1
    return tally