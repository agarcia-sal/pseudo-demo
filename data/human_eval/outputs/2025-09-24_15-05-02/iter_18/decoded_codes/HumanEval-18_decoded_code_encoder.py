from typing import Union

def how_many_times(string: Union[str, bytes], substring: Union[str, bytes]) -> int:
    times = 0
    length_string = len(string)
    length_substring = len(substring)
    if length_substring == 0 or length_substring > length_string:
        return 0
    for i in range(length_string - length_substring + 1):
        if string[i:i + length_substring] == substring:
            times += 1
    return times