def how_many_times(string: str, substring: str) -> int:
    times = 0
    string_length = len(string)
    substring_length = len(substring)
    max_index = string_length - substring_length + 1
    i = 0
    while i < max_index:
        current_slice = ""
        j = 0
        while j < substring_length:
            current_slice += string[i + j]
            j += 1
        if current_slice == substring:
            times += 1
        i += 1
    return times