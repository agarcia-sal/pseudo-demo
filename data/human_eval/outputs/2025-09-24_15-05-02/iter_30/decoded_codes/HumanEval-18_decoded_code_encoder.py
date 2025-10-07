def how_many_times(string: str, substring: str) -> int:
    if not substring:
        return 0
    times = 0
    limit = len(string) - len(substring) + 1
    for i in range(limit):
        if string[i:i + len(substring)] == substring:
            times += 1
    return times