def count_upper(string_input: str) -> int:
    total_upper: int = 0
    position: int = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    while position < len(string_input):
        if string_input[position] in vowels:
            total_upper += 1
        position += 2
    return total_upper