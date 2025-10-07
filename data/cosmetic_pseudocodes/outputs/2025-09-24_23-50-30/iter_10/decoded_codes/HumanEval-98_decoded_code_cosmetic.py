def count_upper(string_input: str) -> int:
    count_accumulator: int = 0
    position: int = 0
    vowels = {"A", "E", "I", "O", "U"}
    while position < len(string_input):
        if string_input[position] in vowels:
            count_accumulator += 1
        position += 2
    return count_accumulator