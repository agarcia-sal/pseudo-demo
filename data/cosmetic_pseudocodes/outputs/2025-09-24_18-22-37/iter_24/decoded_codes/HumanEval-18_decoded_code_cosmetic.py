def how_many_times(original_string: str, target_substring: str) -> int:
    total_matches: int = 0
    start_pos: int = 0
    max_pos: int = len(original_string) - len(target_substring)
    while start_pos <= max_pos:
        current_candidate: str = original_string[start_pos : start_pos + len(target_substring)]
        if current_candidate == target_substring:
            total_matches += 1
        start_pos += 1
    return total_matches