def is_palindrome(string_input: str) -> bool:
    length_var: int = len(string_input)
    position_var: int = 0
    while position_var < length_var:
        opposite_pos: int = (length_var - 1) - position_var
        char_front: str = string_input[position_var]
        char_back: str = string_input[opposite_pos]
        if char_front != char_back:
            return False
        position_var += 1
    return True