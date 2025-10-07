def how_many_times(string: str, substring: str) -> int:
    times = 0
    string_length = len(string)
    substring_length = len(substring)
    loop_limit = string_length - substring_length + 1
    for i in range(loop_limit):
        segment = ''
        for j in range(substring_length):
            segment += string[i + j]
        if segment == substring:
            times += 1
    return times