def count_upper(text_arg: str) -> int:
    total: int = 0
    position: int = 0
    vowels = {"A", "E", "I", "O", "U"}
    while position < len(text_arg):
        current_char = text_arg[position]
        if current_char in vowels:
            total += 1
        position += 2
    return total