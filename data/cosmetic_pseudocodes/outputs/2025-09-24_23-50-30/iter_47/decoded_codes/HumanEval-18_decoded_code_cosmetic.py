def how_many_times(original_string: str, target_substring: str) -> int:
    acc: int = 0
    upper_bound: int = len(original_string) - len(target_substring)
    pos: int = 0
    while pos <= upper_bound:
        if original_string[pos : pos + len(target_substring)] == target_substring:
            acc += 1
        pos += 1
    return acc