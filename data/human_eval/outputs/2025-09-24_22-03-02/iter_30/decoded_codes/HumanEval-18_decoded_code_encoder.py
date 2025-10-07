def how_many_times(string: str, substring: str) -> int:
    times = 0
    length_string = len(string)
    length_substring = len(substring)
    limit = length_string - length_substring + 1
    for i in range(limit):
        current_slice = ''
        for j in range(i, i + length_substring):
            current_slice += string[j]
        if current_slice == substring:
            times += 1
    return times