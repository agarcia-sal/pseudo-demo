def how_many_times(string: str, substring: str) -> int:
    times = 0
    for index in range(len(string) - len(substring) + 1):
        if string[index:index + len(substring)] == substring:
            times += 1
    return times