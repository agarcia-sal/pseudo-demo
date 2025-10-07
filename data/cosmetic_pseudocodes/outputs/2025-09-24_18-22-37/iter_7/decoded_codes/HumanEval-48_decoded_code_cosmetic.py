def is_palindrome(str: str) -> bool:
    length_val = len(str)
    pos = 0
    while pos < length_val:
        front_char = str[pos]
        back_index = length_val - 1 - pos
        back_char = str[back_index]
        if front_char != back_char:
            return False
        pos += 1
    return True