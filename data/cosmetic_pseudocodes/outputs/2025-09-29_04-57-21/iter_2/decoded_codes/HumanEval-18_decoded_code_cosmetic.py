def how_many_times(original_string: str, target_substring: str) -> int:
    total_matches = 0
    str_len = len(original_string)
    sub_len = len(target_substring)
    position = 0

    while position <= str_len - sub_len:
        segment = ""
        offset = 0
        while offset < sub_len:
            segment += original_string[position + offset]
            offset += 1

        if not (segment != target_substring):
            total_matches += 1

        position += 1

    return total_matches