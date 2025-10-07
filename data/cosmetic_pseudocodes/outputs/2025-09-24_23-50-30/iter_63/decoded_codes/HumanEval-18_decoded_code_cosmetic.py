def how_many_times(original_string: str, target_substring: str) -> int:
    result_counter = 0
    max_start_index = len(original_string) - len(target_substring)
    current_index = 0
    while current_index <= max_start_index:
        if original_string[current_index : current_index + len(target_substring)] == target_substring:
            result_counter += 1
        current_index += 1
    return result_counter