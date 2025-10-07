def is_palindrome(str_input: str) -> bool:
    len_var: int = len(str_input)
    pos_var: int = 0

    while pos_var < len_var:
        char_front: str = str_input[pos_var]
        rev_pos: int = len_var - 1 - pos_var
        char_back: str = str_input[rev_pos]

        if char_front != char_back:
            return False

        pos_var += 1

    return True