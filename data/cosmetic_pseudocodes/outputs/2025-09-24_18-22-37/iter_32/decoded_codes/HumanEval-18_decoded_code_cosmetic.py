def how_many_times(original_string: str, target_substring: str) -> int:
    tally: int = 0
    max_start: int = len(original_string) - len(target_substring)
    pos: int = 0

    while pos <= max_start:
        segment: str = original_string[pos : pos + len(target_substring)]
        if segment == target_substring:
            tally += 1
        pos += 1

    return tally