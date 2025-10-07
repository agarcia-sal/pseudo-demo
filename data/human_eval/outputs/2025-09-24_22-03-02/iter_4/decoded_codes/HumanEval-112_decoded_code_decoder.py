def reverse_delete(s: str, c: str) -> tuple[str, bool]:
    filtered_string = ''.join(ch for ch in s if ch not in c)
    is_palindrome = filtered_string == filtered_string[::-1]
    return (filtered_string, is_palindrome)