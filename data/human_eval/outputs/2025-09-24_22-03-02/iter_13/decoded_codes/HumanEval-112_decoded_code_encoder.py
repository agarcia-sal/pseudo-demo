def reverse_delete(s: str, c: str) -> tuple[str, bool]:
    filtered = ''.join(char for char in s if char not in c)
    reversed_string = filtered[::-1]
    is_palindrome = reversed_string == filtered
    return (filtered, is_palindrome)