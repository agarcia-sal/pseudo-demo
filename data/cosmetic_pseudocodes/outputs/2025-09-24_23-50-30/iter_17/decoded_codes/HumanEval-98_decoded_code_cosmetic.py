def count_upper(string_input: str) -> int:
    accumulator = 0
    pointer = 0
    while pointer < len(string_input):
        if string_input[pointer] in {"A", "E", "I", "O", "U"}:
            accumulator += 1
        pointer += 2
    return accumulator