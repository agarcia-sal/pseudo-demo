def count_upper(string_input: str) -> int:
    tally: int = 0
    position: int = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    while position < len(string_input):
        if string_input[position] in vowels:
            tally += 1
        position += 2
    return tally