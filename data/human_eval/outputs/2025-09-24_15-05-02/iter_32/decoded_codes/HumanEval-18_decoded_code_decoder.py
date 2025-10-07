def how_many_times(string: str, substring: str) -> int:
    times = 0
    max_start = len(string) - len(substring)
    for index in range(max_start + 1):
        if string[index : index + len(substring)] == substring:
            times += 1
    return times