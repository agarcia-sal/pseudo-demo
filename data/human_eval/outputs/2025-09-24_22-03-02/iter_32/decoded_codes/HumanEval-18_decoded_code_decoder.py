def how_many_times(string: str, substring: str) -> int:
    times = 0
    string_length = len(string)
    substring_length = len(substring)
    max_index = string_length - substring_length + 1

    for i in range(max_index):
        match = True
        for j in range(substring_length):
            if string[i + j] != substring[j]:
                match = False
                break
        if match:
            times += 1

    return times