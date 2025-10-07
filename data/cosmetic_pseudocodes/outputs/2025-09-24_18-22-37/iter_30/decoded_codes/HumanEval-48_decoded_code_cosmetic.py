def is_palindrome(string: str) -> bool:
    counter: int = 0
    upper_limit: int = len(string) - 1
    while counter <= upper_limit:
        front_char: str = string[counter]
        back_char: str = string[upper_limit - counter]
        if front_char != back_char:
            return False
        counter += 1
    return True