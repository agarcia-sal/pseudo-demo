def check_if_last_char_is_a_letter(input_string: str) -> bool:
    word_collection = input_string.split(' ')
    terminal_piece = word_collection[-1]
    # Check if terminal_piece is exactly one character long and is a lowercase letter a-z
    return len(terminal_piece) == 1 and 'a' <= terminal_piece.lower() <= 'z'