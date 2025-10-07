from typing import AnyStr

def how_many_times(string: AnyStr, substring: AnyStr) -> int:
    if not substring or not string or len(substring) > len(string):
        return 0
    times: int = 0
    length_substring: int = len(substring)
    length_string: int = len(string)
    # Iterate over valid start indices where substring can fit entirely
    for i in range(length_string - length_substring + 1):
        if string[i : i + length_substring] == substring:
            times += 1
    return times