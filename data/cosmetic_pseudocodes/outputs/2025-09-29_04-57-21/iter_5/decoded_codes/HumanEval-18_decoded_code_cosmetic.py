def how_many_times(original_string: str, target_substring: str) -> int:
    counter: int = 0
    position: int = 0
    target_len: int = len(target_substring)
    max_start: int = len(original_string) - target_len
    while position <= max_start:
        if original_string[position:position + target_len] == target_substring:
            counter += 1
        position += 1
    return counter