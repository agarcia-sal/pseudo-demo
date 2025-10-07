def count_upper(string_input: str) -> int:
    accumulator: int = 0
    iterator: int = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    while iterator < len(string_input):
        if string_input[iterator] in vowels:
            accumulator += 1
        iterator += 2
    return accumulator