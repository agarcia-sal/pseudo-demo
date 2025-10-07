def reverse_delete(s: str, c: str) -> tuple[str, bool]:
    temp_string = ''.join(char for char in s if char not in c)
    reversed_temp_string = temp_string[::-1]
    is_palindrome = reversed_temp_string == temp_string
    return temp_string, is_palindrome