def is_palindrome(string_var: str) -> bool:
    integer_var1: int = 0
    integer_var2: int = len(string_var) - 1
    while True:
        if integer_var1 > integer_var2:
            break

        char_a: str = string_var[integer_var1]
        char_b: str = string_var[integer_var2]

        if char_a != char_b:
            return False

        integer_var1 += 1
        integer_var2 -= 1
    return True