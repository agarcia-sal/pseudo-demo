def is_palindrome(inputStr: str) -> bool:
    position: int = 0
    length_val: int = len(inputStr)  # length computed once for efficiency
    while position < length_val:
        front_char: str = inputStr[position]
        back_index: int = length_val - 1 - position
        back_char: str = inputStr[back_index]
        if front_char != back_char:
            return False
        position += 1
    return True