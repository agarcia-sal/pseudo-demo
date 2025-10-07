def how_many_times(string: str, substring: str) -> int:
    times = 0
    limit = len(string) - len(substring) + 1
    for i in range(limit):
        current_slice = ""
        for j in range(i, i + len(substring)):
            current_slice += string[j]
        if current_slice == substring:
            times += 1
    return times