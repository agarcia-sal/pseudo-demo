def how_many_times(string: str, substring: str) -> int:
    times = 0
    limit = len(string) - len(substring) + 1
    for i in range(limit):
        segment = string[i:i+len(substring)]
        if segment == substring:
            times += 1
    return times