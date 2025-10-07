def count_upper(string_input: str) -> int:
    accumulator: int = 0
    pointer: int = 0
    while pointer < len(string_input):
        if string_input[pointer] in "AEIOU":
            accumulator += 1
        pointer += 2
    return accumulator