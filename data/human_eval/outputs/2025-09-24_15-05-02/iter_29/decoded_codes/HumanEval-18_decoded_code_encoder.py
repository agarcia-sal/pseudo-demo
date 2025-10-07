def how_many_times(string: str, substring: str) -> int:
    times = 0
    substring_length = len(substring)
    if substring_length == 0:
        return 0
    for index in range(len(string) - substring_length + 1):
        if string[index : index + substring_length] == substring:
            times += 1
    return times