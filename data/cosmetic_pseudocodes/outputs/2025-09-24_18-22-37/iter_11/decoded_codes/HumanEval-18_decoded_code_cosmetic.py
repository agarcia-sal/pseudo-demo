def how_many_times(original_string: str, target_substring: str) -> int:
    tally: int = 0
    start_position: int = 0
    max_start: int = len(original_string) - len(target_substring)
    while start_position <= max_start:
        candidate_piece = original_string[start_position : start_position + len(target_substring)]
        if candidate_piece == target_substring:
            tally += 1
        start_position += 1
    return tally