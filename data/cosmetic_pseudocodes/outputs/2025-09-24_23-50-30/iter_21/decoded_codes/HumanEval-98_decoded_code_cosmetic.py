def count_upper(string_input: str) -> int:
    total_upper: int = 0
    current_position: int = 0
    vowels = {"A", "E", "I", "O", "U"}

    while current_position < len(string_input):
        if string_input[current_position] in vowels:
            total_upper += 1
        current_position += 2

    return total_upper