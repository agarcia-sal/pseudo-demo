def how_many_times(string: str, substring: str) -> int:
    times = 0
    string_length = len(string)
    substring_length = len(substring)
    limit = string_length - substring_length + 1

    for i in range(limit):
        match_substring = ''
        for j in range(substring_length):
            current_char = string[i + j]
            match_substring += current_char

        if match_substring == substring:
            times += 1

    return times