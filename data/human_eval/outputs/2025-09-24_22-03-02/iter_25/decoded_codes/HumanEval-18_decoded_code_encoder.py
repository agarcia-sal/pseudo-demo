def how_many_times(string: str, substring: str) -> int:
    times = 0
    string_length = len(string)
    substring_length = len(substring)
    upper_limit = string_length - substring_length + 1
    for i in range(upper_limit):
        matches_substring = True
        for j in range(substring_length):
            if string[i + j] != substring[j]:
                matches_substring = False
                break
        if matches_substring:
            times += 1
    return times