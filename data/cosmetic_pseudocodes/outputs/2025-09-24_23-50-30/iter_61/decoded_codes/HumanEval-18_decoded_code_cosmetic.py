def how_many_times(original_string: str, target_substring: str) -> int:
    result: int = 0
    boundary: int = len(original_string) - len(target_substring)
    position: int = 0
    while True:
        if position > boundary:
            break
        elif original_string[position:position + len(target_substring)] != target_substring:
            position += 1
        else:
            result += 1
            position += 1
    return result