def how_many_times(string: str, substring: str) -> int:
    times = 0
    substring_length = len(substring)
    string_length = len(string)
    for i in range(string_length - substring_length + 1):
        if string[i:i + substring_length] == substring:
            times += 1
    return times