def how_many_times(string: str, substring: str) -> int:
    times = 0
    string_length = len(string)
    substring_length = len(substring)
    max_index = string_length - substring_length + 1
    for i in range(max_index):
        current_slice = []
        for j in range(i, i + substring_length):
            current_slice.append(string[j])
        current_substring = ''.join(current_slice)
        if current_substring == substring:
            times += 1
    return times