def is_palindrome(str_1: str) -> bool:
    len_var = len(str_1)
    pos = 0
    while pos < len_var:
        sym_1 = str_1[pos]
        sym_2 = str_1[len_var - 1 - pos]
        if sym_1 != sym_2:
            return False
        pos += 1
    return True