def reverse_delete(s: str, c: str) -> tuple[str, bool]:
    result_string = ''.join(char for char in s if char not in c)
    is_palindrome = result_string == result_string[::-1]
    return result_string, is_palindrome