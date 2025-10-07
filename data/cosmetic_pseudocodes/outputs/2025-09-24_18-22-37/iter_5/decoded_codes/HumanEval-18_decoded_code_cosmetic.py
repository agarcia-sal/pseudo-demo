def how_many_times(source_str: str, search_str: str) -> int:
    total_occurrences: int = 0
    max_start_index: int = len(source_str) - len(search_str)
    current_pos: int = 0
    while current_pos <= max_start_index:
        # Check if the substring matches search_str
        if source_str[current_pos : current_pos + len(search_str)] == search_str:
            total_occurrences += 1
        current_pos += 1
    return total_occurrences