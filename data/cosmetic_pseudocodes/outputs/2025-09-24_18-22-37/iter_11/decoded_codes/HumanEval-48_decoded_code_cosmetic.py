def is_palindrome(input_string: str) -> bool:
    str_length: int = len(input_string)
    position_counter: int = 0

    while position_counter < str_length:
        front_char: str = input_string[position_counter]
        back_char_pos: int = str_length - 1 - position_counter
        back_char: str = input_string[back_char_pos]

        if front_char != back_char:
            return False

        position_counter += 1

    return True