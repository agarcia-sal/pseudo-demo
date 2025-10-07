def how_many_times(string: str, substring: str) -> int:
    times = 0
    string_length = len(string)
    substring_length = len(substring)
    max_index = string_length - substring_length + 1
    for i in range(max_index):
        match_substring = [string[i + j] for j in range(substring_length)]
        substring_chars = [substring[k] for k in range(substring_length)]
        if match_substring == substring_chars:
            times += 1
    return times