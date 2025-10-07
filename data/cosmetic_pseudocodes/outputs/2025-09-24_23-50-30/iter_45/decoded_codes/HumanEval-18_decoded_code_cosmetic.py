def how_many_times(original_string: str, target_substring: str) -> int:
    total_length: int = len(original_string)
    search_length: int = len(target_substring)
    current_index: int = 0
    found_count: int = 0

    while current_index <= total_length - search_length:
        # Check if the substring equals the target substring
        if original_string[current_index : current_index + search_length] == target_substring:
            found_count += 1
        current_index += 1

    return found_count