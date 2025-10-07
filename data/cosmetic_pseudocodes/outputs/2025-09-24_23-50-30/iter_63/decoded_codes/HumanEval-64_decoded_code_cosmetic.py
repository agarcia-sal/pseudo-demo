from typing import Union

def vowels_count(string_input: str) -> int:
    symbols: str = "aeiouAEIOU"
    tally: int = 0
    for position in range(len(string_input)):
        if string_input[position] in symbols:
            tally += 1
    if string_input and string_input[-1] in ('y', 'Y'):
        tally += 1
    return tally