def reverse_delete(s: str, c: str) -> tuple[str, bool]:
    s_filtered = ''.join(char for char in s if char not in c)
    s = s_filtered
    s_reversed = s[::-1]
    is_palindrome = s_reversed == s
    return s, is_palindrome