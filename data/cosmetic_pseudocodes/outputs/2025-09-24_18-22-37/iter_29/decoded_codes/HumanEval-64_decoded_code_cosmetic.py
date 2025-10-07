from typing import Union

def vowels_count(string_input: str) -> int:
    vowel_list = "AEIOUaeiou"
    idx = 0
    count = 0
    while idx < len(string_input):
        curr_char = string_input[idx]
        if curr_char in vowel_list:
            count += 1
        idx += 1
    if string_input and string_input[-1] in ('y', 'Y'):
        count += 1
    return count