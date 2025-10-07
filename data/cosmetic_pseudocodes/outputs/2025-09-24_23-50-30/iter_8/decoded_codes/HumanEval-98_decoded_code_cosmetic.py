def count_upper(string_input: str) -> int:
    tally: int = 0
    step_index: int = 0
    while step_index < len(string_input):
        if string_input[step_index] in "AEIOU":
            tally += 1
        step_index += 2
    return tally