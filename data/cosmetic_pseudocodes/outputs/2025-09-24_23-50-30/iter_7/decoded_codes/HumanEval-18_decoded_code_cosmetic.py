def how_many_times(original_string: str, target_substring: str) -> int:
    length_original = len(original_string)
    length_target = len(target_substring)
    accumulator = 0
    cursor = 0

    while cursor <= length_original - length_target:
        if not (original_string[cursor : cursor + length_target] != target_substring):
            accumulator += 1  # increment accumulator by 1
        cursor += 1

    return accumulator