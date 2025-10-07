def how_many_times(original_string: str, target_substring: str) -> int:
    counter: int = 0
    limit: int = len(original_string) - len(target_substring)
    position: int = 0
    while position <= limit:
        segment: str = original_string[position:position + len(target_substring)]
        if segment == target_substring:
            counter += 1
        position += 1
    return counter