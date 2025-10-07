def how_many_times(original_string: str, target_substring: str) -> int:
    tally: int = 0
    max_start: int = len(original_string) - len(target_substring)
    position: int = 0
    while position <= max_start:
        if original_string[position : position + len(target_substring)] == target_substring:
            tally += 1
        position += 1
    return tally