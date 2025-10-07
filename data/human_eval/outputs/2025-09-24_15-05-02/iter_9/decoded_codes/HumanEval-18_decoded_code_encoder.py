def how_many_times(string, substring):
    times = 0
    max_start_index = len(string) - len(substring)
    for index in range(max_start_index + 1):
        if string[index:index + len(substring)] == substring:
            times += 1
    return times