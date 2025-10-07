def how_many_times(string: str, substring: str) -> int:
    times = 0
    string_length = len(string)
    substring_length = len(substring)
    iteration_limit = string_length - substring_length + 1
    for i in range(iteration_limit):
        current_slice = ''
        for j in range(substring_length):
            current_slice += string[i + j]
        if current_slice == substring:
            times += 1
    return times