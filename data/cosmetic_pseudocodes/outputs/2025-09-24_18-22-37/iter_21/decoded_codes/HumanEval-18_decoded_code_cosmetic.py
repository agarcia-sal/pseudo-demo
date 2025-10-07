def how_many_times(original_string: str, target_substring: str) -> int:
    match_total: int = 0
    max_start_position: int = len(original_string) - len(target_substring)
    current_position: int = 0
    while current_position <= max_start_position:
        substring_piece: str = ""
        counter_j: int = 0
        segment_length: int = len(target_substring)
        while counter_j < segment_length:
            substring_piece += original_string[current_position + counter_j]
            counter_j += 1
        if substring_piece == target_substring:
            match_total += 1
        current_position += 1
    return match_total