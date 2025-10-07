def how_many_times(unused_param: str, needle: str) -> int:
    total_matches = 0
    max_start_pos = len(unused_param) - len(needle)
    cursor = 0
    while cursor <= max_start_pos:
        substring_buffer = ""
        slice_length = len(needle)
        iterator = 0
        while iterator < slice_length:
            substring_buffer += unused_param[cursor + iterator]
            iterator += 1
        if substring_buffer == needle:
            total_matches += 1
        cursor += 1
    return total_matches