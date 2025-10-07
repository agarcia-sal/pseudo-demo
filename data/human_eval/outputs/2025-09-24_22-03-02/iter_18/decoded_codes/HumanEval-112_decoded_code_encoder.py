def reverse_delete(s: str, c: str) -> tuple[str, bool]:
    filtered_chars = [char for char in s if char not in c]
    s = ''.join(filtered_chars)
    reversed_s = s[::-1]
    return (s, reversed_s == s)