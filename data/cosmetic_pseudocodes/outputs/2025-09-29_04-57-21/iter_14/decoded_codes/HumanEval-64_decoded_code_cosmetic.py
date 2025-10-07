def vowels_count(string_input: str) -> int:
    vowel_set = "AEIOUaeiou"
    tally = 0
    idx = 0
    while idx < len(string_input):
        curr_char = string_input[idx]
        if curr_char in vowel_set:
            tally += 1
        idx += 1
    last_char = string_input[-1] if string_input else ''
    if last_char in ('Y', 'y'):
        tally += 1
    return tally